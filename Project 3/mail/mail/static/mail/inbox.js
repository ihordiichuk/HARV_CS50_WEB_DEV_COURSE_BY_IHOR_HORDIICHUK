document.addEventListener('DOMContentLoaded', function () {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#email-detail-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  // Handle form submission
  document.querySelector('#compose-form').onsubmit = function (event) {
    event.preventDefault();

    // Collect form data
    const recipients = document.querySelector('#compose-recipients').value;
    const subject = document.querySelector('#compose-subject').value;
    const body = document.querySelector('#compose-body').value;

    // Send POST request to API
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body
      })
    })
      .then(response => response.json())
      .then(result => {
        // Redirect to 'Sent' mailbox on success
        load_mailbox('sent');
      });

    return false;
  }
}

function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#email-detail-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';

  // Set the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Fetch emails from the API for the selected mailbox
  fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {
      // Iterate over each email returned by the API
      emails.forEach(email => {
        // Create a container for the email.preview
        const emailDiv = document.createElement('div');
        emailDiv.className = 'email-item';
        emailDiv.style.border = '1px solid #ccc';
        emailDiv.style.padding = '10px';
        emailDiv.style.marginBottom = '8px';
        emailDiv.style.cursor = 'pointer';

        // Set background color based on read status
        emailDiv.style.backgroundColor = email.read ? '#f0f0f0' : 'white';

        // Fill the preview block with sender, subject, and timestamp
        emailDiv.innerHTML = `
          <strong>${email.sender}</strong> - ${email.subject}
          <span style="float: right;">${email.timestamp}</span>`;

        // Add click event to open the full email view
        emailDiv.addEventListener('click', () => load_email(email.id));

        // Append the preview to the emails-view
        document.querySelector('#emails-view').appendChild(emailDiv);
      });
    });
}

function load_email(email_id) {

  // Clear and show the email-detail-view
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-detail-view').style.display = 'block';
  document.querySelector('#email-detail-view').innerHTML = '';

  // Fetch the email by ID
  fetch(`/emails/${email_id}`)
    .then(response => response.json())
    .then(email => {

      // Mark the email as read
      fetch(`/emails/${email_id}`, {
        method: 'PUT',
        body: JSON.stringify({ read: true })
      });

      // Create email detail elements
      const container = document.createElement('div');
      container.innerHTML = `
        <p><strong>From:</strong> ${email.sender}</p>
        <p><strong>To:</strong> ${email.recipients.join(', ')}</p>
        <p><strong>Subject:</strong> ${email.subject}</p>
        <p><strong>Timestamp:</strong> ${email.timestamp}</p>
        <hr>
        <p>${email.body.replace(/\n/g, '<br>')}</p>
      `;

      // Create Archive/Unarchive button if not Sent mailbox
      if (email.sender !== document.querySelector('strong').innerText) {
        const archiveButton = document.createElement('button');
        archiveButton.className = 'btn btn-sm btn-outline-primary';
        archiveButton.innerText = email.archived ? 'Unarchive' : 'Archive';

        archiveButton.addEventListener('click', () => {
          fetch(`/emails/${email_id}`, {
            method: 'PUT',
            body: JSON.stringify({
              archived: !email.archived
            })
          })
            .then(() => load_mailbox('inbox'));
        })

        container.appemdChild(document.createElement('hr'));
        container.appendChild(archiveButton);
      }

      // Append to the email-detail-view
      document.querySelector('#email-detail-view').appendChild(container);
    });
}