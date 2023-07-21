import React, { useState, useRef } from "react";

import emailjs from "@emailjs/browser";

import "./Contact.css";
export default function Contact() {
  const form = useRef();
  const [text, setText] = useState("");

  const sendEmail = (e) => {
    e.preventDefault();
    let msg = document.getElementById("msg");
    let name = document.getElementById("name");
    let email = document.getElementById("email");
    let phone = document.getElementById("phone");
    let work = document.getElementById("work");
    let detail = document.getElementById("detail");
    console.log("yoo");
    emailjs
      .sendForm(
        "service_mid2gs3",
        "template_vvfcpwh",
        form.current,
        "IFYJJ44BSFPlqZ2Hv"
      )
      .then(
        (result) => {
          console.log(result.text);
          setText("Success: Successfully submitted");
          msg.style.color = "green";
          msg.style.backgroundColor = "#def2d6";
          msg.style.borderColor = "green";
          msg.style.display = "block";
          if (name.value != null) {
            name.value = "";
          }
          if (email.value != null) {
            email.value = "";
          }
          if (phone.value != null) {
            phone.value = "";
          }
          if (work.value != null) {
            work.value = "";
          }
          if (detail.value != null) {
            detail.value = "";
          }
        },
        (error) => {
          console.log(error.text);
        }
      );
    setInterval(() => {
      msg.style.display = "none";
    }, 5000);
  };

  document.title = "Avinash Sharma | Contact Me";

  // const Submit = (e) => {
  //   e.preventDefault();
  //   sendEmail("Avinas", "aviansn");
  // };
  // const Submit = (e) => {
  //   e.preventDefault();
  //   // let submit=false;

  //   let name = document.getElementById("name");
  //   let email = document.getElementById("email");
  //   let phone = document.getElementById("phone");
  //   let work = document.getElementById("work");
  //   let detail = document.getElementById("detail");
  //   let msg = document.getElementById("msg");
  //   let formBtn = document.getElementById("formBtn");

  //   if (
  //     3 <= name.value.length &&
  //     30 >= name.value.length &&
  //     30 >= email.value.length &&
  //     11 >= phone.value.length &&
  //     50 >= work.value.length &&
  //     200 >= detail.value.length &&
  //     4 <= email.value.length &&
  //     8 <= phone.value.length &&
  //     3 <= work.value.length &&
  //     5 <= detail.value.length
  //   ) {
  //     let regname = /^[A-Za-z]+[A-Za-z]$/;
  //     let resultname = regname.test(name.value);
  //     // console.log(result);
  //     let regemail = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
  //     let resultemail = regemail.test(email.value);
  //     // console.log(result);
  //     if (resultname && resultemail) {
  //       // success
  //       setText("Success: Successfully submitted");
  //       msg.style.color = "green";
  //       msg.style.backgroundColor = "#def2d6";
  //       msg.style.borderColor = "green";
  //       msg.style.display = "block";
  //       console.log(111111111)
  //       formBtn.disabled = true;
  //       // formBtn.onClick = "none";
  //     } else {
  //       setText("Please enter in corect format");
  //       msg.style.color = "#b32f2d";
  //       msg.style.backgroundColor = "#ecc8c5";
  //       msg.style.borderColor = "#b32f2d";
  //       msg.style.display = "block";
  //     }
  //   } else {
  //     setText("Error: Please enter in correct format");
  //     msg.style.color = "#b32f2d";
  //     msg.style.backgroundColor = "#ecc8c5";
  //     msg.style.display = "block";
  //   }
  //   setInterval(() => {
  //     msg.style.display = "none";
  //   }, 5000);
  //   setInterval(() => {
  //     msg.style.display = "none";
  //     formBtn.disabled = false;

  //   }, 10000);
  // };
  return (
    <>
      <div className="msgBox">
        <div id="msg">{text}</div>
      </div>
      <div className="ContactHeadBox ">
        <hr></hr>

        <div className="ContactHead">
          Contact &nbsp;<span>Me</span>
        </div>
        <hr className="hr"></hr>
      </div>
      <div className="contactBox">
        <form ref={form} method="post" onSubmit={sendEmail}>
          <div className="contactTable1">
            <label htmlFor="name">Full Name | Comapany Name</label>{" "}
            <input
              placeholder="Enter name (min 3 and max 30)"
              name="user_name"
              id="name"
              type="text"
              pattern="^[A-Z a-z]{3,30}[A-Z a-z]$"
              required
            />
          </div>
          <div className="contactTable2">
            <label htmlFor="email">Email ID</label>{" "}
            <input
              placeholder="Enter email "
              name="user_email"
              id="email"
              type="text"
              pattern="^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"
              required
            />
          </div>
          <div className="contactTable3">
            <label htmlFor="phone">Phone No.</label>{" "}
            <input
              placeholder="Enter phone number "
              name="user_phone"
              id="phone"
              type="text"
              pattern="^[0-9]{8,12}"
              required
            />
          </div>
          <div className="contactTable4">
            <label htmlFor="work">Work </label>{" "}
            <input
              placeholder="Enter work title"
              name="user_work"
              id="work"
              type="text"
              pattern="^[A-Z0-9 a-z]{3,50}"
              required
            />
          </div>
          <div className="contactTable5">
            <label htmlFor="detail">Message</label>{" "}
            <textarea
              placeholder="Enter work message "
              name="message"
              id="detail"
              type="text"
              rows="4"
              cols="50"
              pattern="^[A-Z0-9 a-z]{3,200}"
              required
            />
          </div>
          <div>
            <div>
              <button className="formBtn" id="formBtn" type="submit">
                Submit
              </button>
              <input className="formBtn" type="reset" />
            </div>
          </div>
        </form>
      </div>
    </>
  );
}
