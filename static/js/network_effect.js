// static/js/network_effect.js

document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('hero-background-canvas');
    if (!canvas) {
        console.error("Canvas element 'hero-background-canvas' not found.");
        return;
    }
    const ctx = canvas.getContext('2d');
    let particles = [];
    const numParticles = 80; // Número de "nós" na rede
    const maxDistance = 100; // Distância máxima para conectar partículas
    const particleSpeed = 0.3; // Velocidade de movimento das partículas

    // Ajusta o tamanho do canvas para o tamanho do contêiner hero
    function resizeCanvas() {
        const heroSection = document.querySelector('.hero');
        canvas.width = heroSection.offsetWidth;
        canvas.height = heroSection.offsetHeight;
    }

    // Objeto Partícula
    class Particle {
        constructor(x, y) {
            this.x = x;
            this.y = y;
            this.size = Math.random() * 2 + 1; // Tamanho entre 1 e 3
            this.speedX = Math.random() * 2 - 1; // Entre -1 e 1
            this.speedY = Math.random() * 2 - 1; // Entre -1 e 1
            this.color = 'rgba(52, 152, 219, 0.8)'; // Cor azul do tema
        }

        update() {
            this.x += this.speedX * particleSpeed;
            this.y += this.speedY * particleSpeed;

            // Inverte a direção se atingir as bordas
            if (this.x > canvas.width || this.x < 0) this.speedX *= -1;
            if (this.y > canvas.height || this.y < 0) this.speedY *= -1;
        }

        draw() {
            ctx.fillStyle = this.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    // Inicializa as partículas
    function init() {
        particles = [];
        for (let i = 0; i < numParticles; i++) {
            const x = Math.random() * canvas.width;
            const y = Math.random() * canvas.height;
            particles.push(new Particle(x, y));
        }
    }

    // Desenha as linhas entre partículas próximas
    function connect() {
        let opacityValue = 1;
        for (let a = 0; a < particles.length; a++) {
            for (let b = a; b < particles.length; b++) {
                let distance = ((particles[a].x - particles[b].x) ** 2 + (particles[a].y - particles[b].y) ** 2) ** 0.5;
                if (distance < maxDistance) {
                    opacityValue = 1 - (distance / maxDistance);
                    ctx.strokeStyle = `rgba(52, 152, 219, ${opacityValue * 0.5})`; // Cor azul com transparência
                    ctx.lineWidth = 1;
                    ctx.beginPath();
                    ctx.moveTo(particles[a].x, particles[a].y);
                    ctx.lineTo(particles[b].x, particles[b].y);
                    ctx.stroke();
                }
            }
        }
    }

    // Loop de animação
    function animate() {
        requestAnimationFrame(animate);
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Limpa o canvas

        for (let i = 0; i < particles.length; i++) {
            particles[i].update();
            particles[i].draw();
        }
        connect();
    }

    // Eventos
    window.addEventListener('resize', () => {
        resizeCanvas();
        init(); // Reinicia as partículas ao redimensionar para evitar problemas
    });

    // Início
    resizeCanvas();
    init();
    animate();
});
