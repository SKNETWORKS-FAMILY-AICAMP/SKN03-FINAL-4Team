import React, { useState, useEffect } from "react";
import SideCard from "./ContactSidecard";
import question from "../../assets/img/question.png";
import Snowfall from "react-snowfall";
import "@fontsource/lexend-deca"; // npm에서 제공하는 경우

const YesPage = () => {
    const questions = [
        {
            question: "어떤 제품군 / 분야를 홍보하고 싶으신가요?",
            options: ["전자제품", "의류", "식품", "기타"],
        },
        {
            question: "예상 금액대를 선택해주세요.",
            options: ["10만원 이하", "10만원 ~ 50만원", "50만원 ~ 100만원", "100만원 이상"],
        },
        {
            question: "원하고자 하는 인플루언서의 메인 활동 플랫폼을 선택해주세요.",
            options: ["인스타그램", "유튜브", "틱톡", "블로그"],
        },
        {
            question: "원하고자 하는 홍보 이벤트를 선택해주세요.",
            options: ["리뷰", "이벤트 진행", "홍보 영상 제작", "기타"],
        },
        {
            question: "원하고자 하는 인플루언서의 성별을 입력해주세요.",
            options: ["남성", "여성", "무관"],
        },
    ];
    const [showSideCard, setShowSideCard] = useState(true);
    const [isMobile, setIsMobile] = useState(window.innerWidth <= 768);
    const [formData, setFormData] = useState({
        companyName: "",
        email: "",
        address: "",
        phone: "",
        contactName: "",
    });
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };
    useEffect(() => {
        const handleResize = () => {
            setShowSideCard(window.innerWidth > 1000); // 768px 이하일 때 SideCard 숨김
            setIsMobile(window.innerWidth <= 768); 
        };

        handleResize(); // 초기 크기 설정
        window.addEventListener("resize", handleResize); // 리사이즈 이벤트 추가
        return () => window.removeEventListener("resize", handleResize); // 이벤트 제거
    }, []);

    return (
        <div
            style={{
                ...styles.container,
                marginLeft: showSideCard ? "45px" : "0", // SideNav가 없으면 marginLeft를 0으로 설정
            }}
        >
            {/* Side Card UI */}
            {showSideCard && <SideCard />}

            {/* 질문 폼 */}
            <div
                style={{
                    ...styles.post,
                    flex: showSideCard ? "2.5" : "3.5", // SideCard가 없을 때 너비 확장
                    marginLeft : isMobile ? "25px" : "40px",
                    marginRight : isMobile ? "-20px" : "0px",
                    marginTop : isMobile ? "20px" : "30px",
                    padding : isMobile ? "20px 10px 10px" : "30px 30px 30px",
                    marginBottom : isMobile ? "15px" : "30px"
                }}
            >
                <Snowfall
                    color="white" // 눈 색상
                    snowflakeCount={150} // 눈송이 개수
                    style={{ zIndex: 9999 }} // 눈이 모든 요소 위에 표시되도록 설정
                />
                
                <div style={styles.section}>Section 1. Bussiness Info</div>
                <div style={styles.sectionLine}></div>
                <form style={styles.form}>
                    <div style={styles.question}>
                        <label style={styles.label}>Q1. 기업명을 입력해주세요.</label>
                        <input
                            type="text"
                            name="companyName"
                            value={formData.companyName}
                            onChange={handleInputChange}
                            style={styles.input}
                            required
                        />
                    </div>
                    <div style={styles.question}>
                        <label style={styles.label}>Q2. 기업 메일 주소를 입력해주세요.</label>
                        <input
                            type="email"
                            name="email"
                            value={formData.email}
                            onChange={handleInputChange}
                            style={styles.input}
                            required
                        />
                    </div>
                    <div style={styles.question}>
                        <label style={styles.label}>Q3. 기업 주소를 입력해주세요.</label>
                        <input
                            type="address"
                            name="address"
                            value={formData.address}
                            onChange={handleInputChange}
                            style={styles.input}
                            required
                        />
                    </div>
                    <div style={styles.question}>
                        <label style={styles.label}>Q4. 담당자 연락처를 입력해주세요.</label>
                        <input
                            type="tel"
                            name="phone"
                            value={formData.phone}
                            onChange={handleInputChange}
                            style={styles.input}
                            required
                        />
                    </div>
                    <div style={styles.question}>
                        <label style={styles.label}>Q5. 담당자명을 입력해주세요.</label>
                        <input
                            type="text"
                            name="contactName"
                            value={formData.contactName}
                            onChange={handleInputChange}
                            style={styles.input}
                            required
                        />
                    </div>
                </form>
                <div style={{...styles.section, background: "linear-gradient(90deg, #A57451 0%, #CDAC7F 33.9%, #E1C897 63.4%, #F5E4AE 100%)"}}>Section 2. Marketing style</div>
                <div style={{...styles.sectionLine, background: "linear-gradient(90deg, #A57451 0%, #CDAC7F 33.9%, #E1C897 63.4%, #F5E4AE 100%)"}}></div>
                    {questions.map((item, index) => (
                        <div key={index} style={styles.question}>
                            <label style={styles.label}>{`Q${index + 1}. ${item.question}`}</label>
                            <select style={styles.select}>
                                {item.options.map((option, idx) => (
                                    <option key={idx} value={option}>
                                        {option}
                                    </option>
                                ))}
                            </select>
                        </div>
                    ))}
                
                <div style={styles.buttoncontainer}>
                    <button type="submit" style={styles.submitButton}>
                        등록
                    </button>
                </div>
            </div>
        </div>
    );
};

const styles = {
    container: {
        display: "flex",
        marginLeft: "45px",
        marginRight: "40px",
        backgroundColor: "#fffaea",
        minHeight: "100vh",
        justifyContent: "space-between", // 좌우 요소 간 여백 균일화
    },
    sideCard: {
        width: "25%",
    },
    post: {
        flex: "2.5",
        background: "linear-gradient(180deg, #FFEFB8 0%, #FFFDF7 25%)",
        marginTop: "30px",
        marginLeft: "40px",
     
        borderRadius: "10px",
        padding: "30px 30px 30px",
        boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
        marginBottom: "30px",
        overflow: "auto",
    },
 
   
    form: {
        display: "flex",
        flexDirection: "column",
        gap: "15px",
       
    },
    question: {
        display: "flex",
        flexDirection: "column",
        gap: "15px",
        marginBottom: "70px"
    },
    label: {
        fontSize: "1.1rem",
        color: "#6d4c41",
        fontWeight: "500"
        
    },
    select: {
        width: "80%",
        padding: "10px",
        borderRadius: "10px",
        border: "1px solid #ddd",
        fontSize: "1rem",
        backgroundColor: "#fff",
        cursor: "pointer",
       
        marginLeft: "20px"
    },
    submitButton: {
        boxSizing: "border-box", // 수정: "box-sizing"의 오타 수정
        width: "80px",
        height: "40px",
        background: "#FBE5A2",
        border: "1px solid #F5E4AE",
        boxShadow: "0px 4px 4px rgba(0, 0, 0, 0.25)",
        borderRadius: "15px",
        cursor: "pointer", // 추가: 버튼 클릭 가능 커서

    },
    contentLine: {
        height: "2px",
        backgroundColor: "#F1D1A3",
        marginBottom: "40px"
    },
    buttoncontainer:{
        display: "flex",
        flexDirection: "column",
        alignItems: "center", // 모든 자식 요소를 가로 중앙 정렬
    },
    input: {
        width: "77%",
        padding: "10px",
        borderRadius: "10px",
        border: "1px solid #ddd",
        fontSize: "1rem",
        backgroundColor: "#fff",
        cursor: "pointer",
       
        marginLeft: "20px"
    },
    section: {
        fontFamily: "'Lexend Deca', sans-serif",
        fontSize: "2rem",
        background: "linear-gradient(90deg, #A57451 0%, #CDAC7F 33.9%, #E1C897 63.4%, #F5E4AE 100%)",
        WebkitBackgroundClip: "text",
        WebkitTextFillColor: "transparent",
       
 
        lineHeight: "1.5", // 줄 간격 설정
     
        
    },
    sectionLine: {
        height: "3px",
        width: "100%",
        background: "linear-gradient(90deg, #A57451 0%, #CDAC7F 33.9%, #E1C897 63.4%, #F5E4AE 100%)",
        marginBottom: "20px"

    }
};

export default YesPage;
