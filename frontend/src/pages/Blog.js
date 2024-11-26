import React, { useEffect, useState } from "react";
import profileImage from "../assets/img/eddy_blog.png";
import axios from "axios";
import Write from "../components/board/SideCard"
import SideCard from "../components/board/SideCard";

const Blog = () => {
    const [posts, setPosts] = useState([]); // 게시글 데이터를 저장할 상태

    useEffect(() => {
        // 서버에서 데이터 가져오기
        const fetchPosts = async () => {
            try {
                const response = await axios.get(process.env.REACT_APP_SERVER_URL); // 서버 API URL
                setPosts(response.data); // 데이터를 상태에 저장
                console.log(response.data)
            } catch (error) {
                console.error("데이터를 가져오는 중 오류 발생:", error);
            }
        };

        fetchPosts(); // 함수 호출
    }, []); // 컴포넌트가 마운트될 때 한 번 실행

    return (
        <div style={styles.container}>
            {/* 왼쪽 사이드바 */}
            {/* <div style={styles.sidebar}>
                <img src={profileImage} alt="Profile" style={styles.profileImage} />
                <h2 style={styles.blogTitle}>Eddy's Blog</h2>
                <p style={styles.description}>Welcome to my blog!</p>
            </div> */}
            <SideCard />
            {/* 오른쪽 게시글 리스트 */}
            <div style={styles.blogList}>
                <div style={styles.blogHeader}>
                    <p style={styles.postCount}>✏️목록</p>
                    <div style={styles.postHeader}>
                        <span style={styles.postNum}>번호</span>
                        <span style={styles.postTitle}>글 제목</span>
                        <span style={styles.postDate}>작성일</span>
                    </div>
                </div>
                <div>
                    {posts.length > 0 ? (
                        posts.map((post, index) => (
                            <div key={post.id} style={styles.postItem}>
                                <span style={styles.postNum}>{index + 1}</span>
                                <span style={styles.postTitle}>{post.title}</span>
                                <span style={styles.postDate}>{post.date}</span>
                            </div>
                        ))
                    ) : (
                        <p style={{ textAlign: "center" }}>게시글이 없습니다.</p>
                    )}
                </div>
            </div>

            {/* write */}
            {/* <Write /> */}
        </div>
    );
};

// 스타일
const styles = {
    container: {
        display: "flex",
        marginLeft: "45px",
        marginRight: "45px",
        backgroundColor: "#fffaea",
        height: "100vh",
    },
    
    blogList: {
        flex: "2.5",
        marginLeft: "40px",
        width: "100%",
        marginTop: "20px"
    },
    blogHeader: {
        borderBottom: "2px solid #F1D1A3",
        paddingBottom: "10px",
        marginBottom: "20px",
       
  
    },
    postCount: {
        fontSize: "1rem",
        marginBottom: "5px",
    },
    postHeader: {
        display: "flex",
        alignItems: "center",
        fontSize: "0.9rem",
        color: "#555",
        marginTop: "5px"
    },
    postNum: {
        flex: "1",
        textAlign: "left",
    },
    postTitle: {
        flex: "5",
        textAlign: "left",
    },
    postDate: {
        flex: "2",
        textAlign: "right",
    },
    postItem: {
        display: "flex",
        justifyContent: "space-between",
        padding: "10px 0",
        borderBottom: "1px solid #f5e4ae",
        fontSize: "0.9rem",
    },
};

export default Blog;
