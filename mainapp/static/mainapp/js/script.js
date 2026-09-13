// Translations
const translations = {
  en: {
    headerText: "Where Curiosity Meets Books",
    aboutTitle: "About Our Library",
    aboutText: "Our school library provides a wide collection of books for students of all grades. Explore, read, and learn new things every day!",
    booksTitle: "Books Collection",
    btnAll: "All",
    btnMath: "Math",
    btnEnglish: "English",
    btnScience: "Science",
    contactTitle: "Contact Us",
    labelFname: "First Name",
    labelLname: "Last Name",
    labelPhone: "Phone Number",
    labelEmail: "Email",
    labelCountry: "Country",
    labelMessage: "Message",
    submitBtn: "Submit",
    visitorTitle: "Website Visitors",
    footerText: "© 2025 School Library. All rights reserved.",
    placeholders: {
      fname: "Your first name..",
      lname: "Your last name..",
      phone: "Your phone number..",
      email: "Your email..",
      message: "Write your message.."
    }
  }
};

// Change language
function changeLanguage(lang) {
  let t = translations[lang];

  document.getElementById("headerText").innerHTML = t.headerText;
  document.getElementById("aboutTitle").innerHTML = t.aboutTitle;
  document.getElementById("aboutText").textContent = t.aboutText;
  document.getElementById("booksTitle").innerHTML = t.booksTitle;
  document.getElementById("btnAll").textContent = t.btnAll;
  document.getElementById("btnMath").textContent = t.btnMath;
  document.getElementById("btnEnglish").textContent = t.btnEnglish;
  document.getElementById("btnScience").textContent = t.btnScience;
  document.getElementById("contactTitle").textContent = t.contactTitle;
  document.getElementById("labelFname").textContent = t.labelFname;
  document.getElementById("labelLname").textContent = t.labelLname;
  document.getElementById("labelPhone").textContent = t.labelPhone;
  document.getElementById("labelEmail").textContent = t.labelEmail;
  document.getElementById("labelCountry").textContent = t.labelCountry;
  document.getElementById("labelMessage").textContent = t.labelMessage;
  document.getElementById("submitBtn").value = t.submitBtn;
  document.getElementById("visitorTitle").textContent = t.visitorTitle;
  document.getElementById("footerText").textContent = t.footerText;

  document.getElementById("fname").placeholder = t.placeholders.fname;
  document.getElementById("lname").placeholder = t.placeholders.lname;
  document.getElementById("phone").placeholder = t.placeholders.phone;
  document.getElementById("email").placeholder = t.placeholders.email;
  document.getElementById("message").placeholder = t.placeholders.message;

  document.body.style.direction = (lang === "ar") ? "rtl" : "ltr";
}

// Filter books by category
function filterBooks(category) {
  const books = document.querySelectorAll('.book');
  books.forEach(book => {
    if(category === 'all' || book.classList.contains(category)) {
      book.style.display = 'block';
    } else {
      book.style.display = 'none';
    }
  });
}
