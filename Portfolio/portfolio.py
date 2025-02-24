import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    st.set_page_config(page_title="Rohit Sharma | Portfolio", page_icon=":computer:", layout="wide")
    
    # Load Lottie animation
    coding_animation = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_jtbfg2nb.json")
    
    # Sidebar - Profile and Contact Info
    st.sidebar.image("Portfolio/Rohit-Image.png", caption="Rohit Sharma", width=250)

    st.sidebar.title("Contact")
    st.sidebar.write("📧 Email: sharmarohits814@gmail.com")
    st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/rohit-sharma-i7/)")
    st.sidebar.write("🐙 [GitHub](https://github.com/rohitshaarma13)")
    st.sidebar.download_button(label="📄 Download Resume", data=b"", file_name="Rohit_Sharma_Resume.pdf", mime="application/pdf")
    
    # Main Content
    st.title("Welcome to My Portfolio! 🚀")
    st.write(
        "Hi, I'm Rohit Sharma, a passionate **Backend Developer** and **Aspiring Data Engineer** with expertise in **Java, SQL, Spring Boot, Power BI, and Python**. "
        "I love building efficient systems and solving complex problems."
    )
    
    # Display animation
    if coding_animation:
        st_lottie(coding_animation, height=200, key="coding")
    
    # Skills Section with Progress Bars
    st.header("Skills")
    skill_data = {"Java & Spring Boot": 90, "SQL & Databases": 85, "Power BI & Data Engineering": 80, "Python & Streamlit": 75}
    for skill, percentage in skill_data.items():
        st.write(f"**{skill}**")
        st.progress(percentage / 100)
    
    # Projects Section
    st.header("Projects")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📚 [Book Haven Store](https://github.com/rohitshaarma13/Book-Haven-Store)")
        st.write("A full-stack bookstore management system built with Java, Spring Boot, Thymeleaf, and SQL.")
    
        st.subheader("📊 [Blinkit Sales Dashboard](https://github.com/rohitshaarma13/Blinkit_Sales_Dashboard)")
        st.write("A data-driven sales dashboard using Power BI and SQL to analyze business performance.")
    
    with col2:
        st.subheader("🖥️ [Employee Management System](https://github.com/rohitshaarma13/Employee_Management_System)")
        st.write("A Java Swing-based desktop application for managing employee records with MySQL integration.")
    
    # Experience Section
    st.header("Experience")
    st.subheader("Codules Technologies Pvt Ltd | Java Developer Intern")
    st.write("Developed multiple desktop-based applications using Java Swing and SQL for data management and user interaction.")
    
    # Achievements
    st.header("Achievements")
    st.write("🏆 **Power BI Certification** - Infosys")
    st.write("🏆 **SQL Certification** - HackerRank")
    st.write("🏆 **Core Java & DSA Certification** - INCAPP")
    st.write("🏆 **4-star rating in Java and SQL on HackerRank")
    
    # Contact Form with CSS Styling
    st.header("Get In Touch")
    contact_form = """
    <style>
        .contact-form input, .contact-form textarea {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        .contact-form button {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .contact-form button:hover {
            background-color: #45a049;
        }
    </style>
    <form class="contact-form" action="https://formsubmit.co/sharmarohits814@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" rows="4" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
    
    # Footer
    st.write("---")
    st.write("Thanks for visiting! Feel free to connect with me.")

if __name__ == "__main__":
    main()
