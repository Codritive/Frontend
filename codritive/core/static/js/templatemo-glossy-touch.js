// ==================== Page Navigation ====================
let currentPage = 'home';
    function showPage(pageId) {
        document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
        document.getElementById(pageId).classList.add('active');

        document.querySelectorAll('.nav-links a').forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('onclick') === `showPage('${pageId}')`) {
                link.classList.add('active');
            }
        });

        currentPage = pageId;

        const footer = document.getElementById('footer');
        const activePage = document.getElementById(pageId);
        activePage.appendChild(footer);

        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    window.addEventListener('DOMContentLoaded', () => {
        const footer = document.getElementById('footer');
        const homePage = document.getElementById('home');
        homePage.appendChild(footer);
    });

    // ==================== Parallax ====================
    document.addEventListener('mousemove', e => {
        const shapes = document.querySelectorAll('.shape');
        const x = e.clientX / window.innerWidth;
        const y = e.clientY / window.innerHeight;

        shapes.forEach((shape, index) => {
            const speed = (index + 1) * 0.5;
            const xPos = (x - 0.5) * speed * 20;
            const yPos = (y - 0.5) * speed * 20;
            shape.style.transform = `translate(${xPos}px, ${yPos}px)`;
        });
    });
            // Add scroll-based animations
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const parallax = document.querySelector('.bg-shapes');
        const speed = scrolled * 0.5;
        parallax.style.transform = `translateY(${speed}px)`;
    });

    // ==================== Form Submission ====================
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(e){
            e.preventDefault();
            const successMsg = document.createElement('div');
            successMsg.style.cssText = `
                position: fixed;
                top:50%; left:50%;
                transform: translate(-50%, -50%);
                background: rgba(46, 204, 113,0.9);
                color:white; padding:20px 40px;
                border-radius:10px; backdrop-filter: blur(20px);
                z-index:10000; animation: fadeIn 0.3s ease;
            `;
            successMsg.textContent = 'Message sent successfully! We\'ll get back to you soon.';
            document.body.appendChild(successMsg);
            setTimeout(()=>successMsg.remove(),3000);
            this.reset();
        });
    }
            // Add ripple animation keyframes
    const style = document.createElement('style');
        style.textContent = `
            @keyframes ripple {
                to {
                    transform: scale(4);
                    opacity: 0;
                }
            }
        `;
    document.head.appendChild(style);
            // Add fade in animation
    const fadeStyle = document.createElement('style');
    fadeStyle.textContent = `
    @keyframes fadeIn {
        from {opacity:0; transform: translate(-50%, -50%) scale(0.8);}
        to {opacity:1; transform: translate(-50%, -50%) scale(1);}
    }`;
    document.head.appendChild(fadeStyle);
// ==================== FAQ ====================
    document.addEventListener('DOMContentLoaded', () => {
        const faqQuestions = document.querySelectorAll('.faq-section .faq-question');
        faqQuestions.forEach(q => {
            q.addEventListener('click', () => {
                const answer = q.nextElementSibling;
                q.classList.toggle('active');
                if (q.classList.contains('active')){
                    answer.style.maxHeight = answer.scrollHeight + "px";
                    answer.style.padding = "15px 20px";
                } else {
                    answer.style.maxHeight = 0;
                    answer.style.padding = "0 20px";
                }
                const arrow = q.querySelector('.icon');
                if (arrow) arrow.classList.toggle('rotate');
            });
        });
    });

    var swiper = new Swiper(".mySwiper", {
        slidesPerView: 3,
        spaceBetween: 20,
        loop: true,
        autoplay: {
        delay: 3000,
        disableOnInteraction: false,
        },
        pagination: {
        el: ".swiper-pagination",
        clickable: true,
        },
        navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
        },
        breakpoints: {
        1024: { slidesPerView: 3 },
        768: { slidesPerView: 2 },
        480: { slidesPerView: 1 },
        },
    });
