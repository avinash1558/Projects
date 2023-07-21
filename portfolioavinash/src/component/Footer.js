import React from "react";
import "./Footer.css";
export default function Footer(props) {
  return (
    <>
      <div className="footer">
        <div className="footerHeadLeft">
          <div className="footerTextBox">
            <div className="footerHeadImg">
              <img src=".//profile-pic.png"></img>
            </div>
            <div className="footerText">{props.footerhead}</div>
          </div>
          <div className="footerTextLine">
            <hr></hr>
          </div>
          <div className="footerTextCom">
            Copyright © 2023 AvinashPortFolio.com
          </div>
        </div>

        <div className="footerHeadright">
          <div>
            <a className="footerIcon" href="/">
              <iconify-icon icon="mingcute:youtube-line"></iconify-icon>
            </a>
          </div>
          <div>
            <a
              className="footerIcon"
              href="https://www.linkedin.com/in/avinash-sharma-0a334825a/"
              target="_blank"
            >
              <iconify-icon icon="mdi:linkedin"></iconify-icon>
            </a>
          </div>
          <div>
            <a className="footerIcon" href="/">
              <iconify-icon icon="mdi:github"></iconify-icon>
            </a>
          </div>
          <div>
            <a className="footerIcon" href="/">
              <iconify-icon icon="mdi:instagram"></iconify-icon>
            </a>
          </div>
        </div>
      </div>
    </>
  );
}
