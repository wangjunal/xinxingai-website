// ====== 导航栏滚动效果 ======
const navbar = document.querySelector('.navbar');
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('navMenu');

window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// 移动端菜单
hamburger.addEventListener('click', () => {
  hamburger.classList.toggle('active');
  navMenu.classList.toggle('active');
});

// 点击导航链接关闭菜单
document.querySelectorAll('.nav-menu a').forEach(link => {
  link.addEventListener('click', () => {
    hamburger.classList.remove('active');
    navMenu.classList.remove('active');
  });
});

// ====== 数字动画 ======
function animateNumbers() {
  const numbers = document.querySelectorAll('.stat-number');
  numbers.forEach(num => {
    const target = parseInt(num.getAttribute('data-target'));
    const duration = 2000;
    const step = Math.ceil(target / (duration / 16));
    let current = 0;

    const update = () => {
      current += step;
      if (current >= target) {
        num.textContent = target;
        return;
      }
      num.textContent = current;
      requestAnimationFrame(update);
    };
    update();
  });
}

// 使用 IntersectionObserver 触发数字动画
const statsSection = document.querySelector('.stats');
if (statsSection) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateNumbers();
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });
  observer.observe(statsSection);
}

// ====== 平滑滚动 ======
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const href = this.getAttribute('href');
    if (href !== '#') {
      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  });
});

// ====== 在线留言表单 ======
const messageForm = document.getElementById('messageForm');
if (messageForm) {
  messageForm.addEventListener('submit', async function(e) {
    e.preventDefault();

    const submitBtn = this.querySelector('.form-submit');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = '发送中...';
    submitBtn.disabled = true;

    // 收集表单数据
    const formData = {
      name: document.getElementById('name').value.trim(),
      phone: document.getElementById('phone').value.trim(),
      gender: document.getElementById('gender').value,
      age: document.getElementById('age').value,
      requirement: document.getElementById('requirement').value.trim()
    };

    // 简单验证
    if (!formData.name) {
      showToast('请填写您的姓名');
      submitBtn.textContent = originalText;
      submitBtn.disabled = false;
      return;
    }
    if (!formData.phone || !/^1\d{10}$/.test(formData.phone)) {
      showToast('请填写正确的手机号码');
      submitBtn.textContent = originalText;
      submitBtn.disabled = false;
      return;
    }

    try {
      // 使用 Formspree 发送邮件到 wangjunal@gmail.com
      const response = await fetch('https://formspree.io/f/mvgoapjj', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: formData.name,
          phone: formData.phone,
          gender: formData.gender,
          age: formData.age,
          requirement: formData.requirement,
          _subject: '心幸爱·喜柿婚恋 - 新留言咨询'
        })
      });

      if (response.ok) {
        showSuccessToast();
        messageForm.reset();
      } else {
        showToast('提交失败，请直接拨打 19329486887 联系我们');
      }
    } catch (err) {
      showToast('网络错误，请直接拨打 19329486887 联系我们');
    } finally {
      submitBtn.textContent = originalText;
      submitBtn.disabled = false;
    }
  });
}

// ====== Toast 提示 ======
function showToast(message) {
  const existing = document.querySelector('.toast');
  if (existing) existing.remove();

  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.innerHTML = `<i class="fas fa-exclamation-circle"></i><h4>提示</h4><p>${message}</p>`;
  document.body.appendChild(toast);

  requestAnimationFrame(() => {
    toast.classList.add('show');
  });

  setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => toast.remove(), 400);
  }, 3000);
}

function showSuccessToast() {
  const existing = document.querySelector('.toast');
  if (existing) existing.remove();

  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.innerHTML = `<i class="fas fa-check-circle"></i><h4>提交成功！</h4><p>感谢您的留言，红娘老师将在24小时内与您联系。</p>`;
  document.body.appendChild(toast);

  requestAnimationFrame(() => {
    toast.classList.add('show');
  });

  setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => toast.remove(), 400);
  }, 4000);
}

// ====== 页面加载动画 ======
document.addEventListener('DOMContentLoaded', () => {
  // 卡片入场动画
  const cards = document.querySelectorAll('.feature-card, .service-card, .case-card, .service-detail-card, .case-detail-card, .event-card, .pricing-card');
  const cardObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
        }, index * 100);
        cardObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  cards.forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(30px)';
    card.style.transition = 'all 0.6s ease';
    cardObserver.observe(card);
  });
});
