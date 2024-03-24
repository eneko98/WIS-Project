const express = require("express");
const nodemailer = require("nodemailer");
const bodyParser = require("body-parser");

const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// POST endpoint to handle subscription form submission
app.post("/subscribe", async (req, res) => {
  const email = req.body.email;
  
  // Send confirmation email
  try {
    let transporter = nodemailer.createTransport({
      // Specify your email service and credentials here
      service: 'gmail',
      auth: {
        user: 'your_email@gmail.com',
        pass: 'your_password'
      }
    });

    let info = await transporter.sendMail({
      from: '"Your Website" <your_email@gmail.com>',
      to: email,
      subject: "Subscription Confirmation",
      text: "Thank you for subscribing to our newsletter!"
    });

    console.log("Email sent: " + info.response);
    res.status(200).send("Confirmation email sent successfully.");
  } catch (error) {
    console.error("Error sending email:", error);
    res.status(500).send("Error sending confirmation email.");
  }
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
