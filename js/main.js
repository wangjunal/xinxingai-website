// ====== 导航栏滚动效果 ======
const navbar = document.querySelector('.navbar');
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('navMenu');

if (navbar) {
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
  });
}

if (hamburger && navMenu) {
  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
  });

  document.querySelectorAll('.nav-menu a').forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('active');
      navMenu.classList.remove('active');
    });
  });
}

// ====== 数字动画 ======
function animateNumbers() {
  const numbers = document.querySelectorAll('.stat-number');
  numbers.forEach(num => {
    const target = parseInt(num.getAttribute('data-target'), 10);
    if (Number.isNaN(target)) return;

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
    if (href && href !== '#') {
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
const FORM_RECIPIENT = 'wangjunal@foxmail.com';
const FORMSPREE_BACKUP_ENDPOINT = 'https://formspree.io/f/mvgoapjj';

if (messageForm) {
  messageForm.addEventListener('submit', async function(e) {
    e.preventDefault();

    const submitBtn = this.querySelector('.form-submit');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = '发送中...';
    submitBtn.disabled = true;

    const formData = collectMessageForm();
    const validationError = validateMessageForm(formData);

    if (validationError) {
      showToast(validationError, 'error');
      submitBtn.textContent = originalText;
      submitBtn.disabled = false;
      return;
    }

    const payload = buildEmailPayload(formData);

    try {
      const sent = await sendMessageToEmail(payload);
      if (sent) {
        showSuccessToast();
        messageForm.reset();
        const privacyAgree = document.getElementById('privacyAgree');
        if (privacyAgree) privacyAgree.checked = true;
        return;
      }

      openMailClient(payload);
      showToast('网络发送未确认，已为您打开邮件客户端备用发送。', 'info');
    } catch (err) {
      openMailClient(payload);
      showToast('网络发送失败，已为您打开邮件客户端备用发送。', 'info');
    } finally {
      submitBtn.textContent = originalText;
      submitBtn.disabled = false;
    }
  });
}

function collectMessageForm() {
  const value = (id) => {
    const el = document.getElementById(id);
    return el ? el.value.trim() : '';
  };

  return {
    name: value('name'),
    phone: value('phone'),
    gender: value('gender'),
    age: value('age'),
    city: value('city'),
    serviceType: value('serviceType') || '红娘婚恋咨询',
    requirement: value('requirement'),
    privacyAgree: Boolean(document.getElementById('privacyAgree')?.checked),
    pageUrl: window.location.href,
    submittedAt: new Date().toLocaleString('zh-CN', { hour12: false })
  };
}

function validateMessageForm(formData) {
  if (!formData.name) return '请填写您的姓名';
  if (!/^1\d{10}$/.test(formData.phone)) return '请填写正确的11位手机号码';
  if (formData.age && (Number(formData.age) < 18 || Number(formData.age) > 80)) return '请填写18到80之间的年龄';
  if (!formData.requirement) return '请简单描述您的需求';
  if (!formData.privacyAgree) return '请勾选信息使用同意项';
  return '';
}

function buildEmailPayload(formData) {
  const subject = `心幸爱·喜柿婚恋 - 新预约咨询 - ${formData.name}`;
  const bodyText = [
    '心幸爱·喜柿婚恋收到一条新的在线预约：',
    '',
    `姓名：${formData.name}`,
    `联系电话：${formData.phone}`,
    `性别：${formData.gender || '未填写'}`,
    `年龄：${formData.age || '未填写'}`,
    `所在地区：${formData.city || '未填写'}`,
    `咨询内容：${formData.serviceType}`,
    `具体需求：${formData.requirement}`,
    '',
    `提交页面：${formData.pageUrl}`,
    `提交时间：${formData.submittedAt}`
  ].join('\n');

  return {
    ...formData,
    subject,
    bodyText,
    recipient: FORM_RECIPIENT
  };
}

async function sendMessageToEmail(payload) {
  try {
    const formSubmitResponse = await fetch(`https://formsubmit.co/ajax/${encodeURIComponent(FORM_RECIPIENT)}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        _subject: payload.subject,
        _template: 'table',
        _captcha: 'false',
        姓名: payload.name,
        联系电话: payload.phone,
        性别: payload.gender || '未填写',
        年龄: payload.age || '未填写',
        所在地区: payload.city || '未填写',
        咨询内容: payload.serviceType,
        具体需求: payload.requirement,
        提交页面: payload.pageUrl,
        提交时间: payload.submittedAt
      })
    });

    if (formSubmitResponse.ok) return true;
  } catch (err) {
    console.warn('FormSubmit send failed, trying backup endpoint.', err);
  }

  let formspreeResponse;
  try {
    formspreeResponse = await fetch(FORMSPREE_BACKUP_ENDPOINT, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        _subject: payload.subject,
        recipient: FORM_RECIPIENT,
        name: payload.name,
        phone: payload.phone,
        gender: payload.gender || '未填写',
        age: payload.age || '未填写',
        city: payload.city || '未填写',
        serviceType: payload.serviceType,
        requirement: payload.requirement,
        submittedAt: payload.submittedAt,
        pageUrl: payload.pageUrl
      })
    });
  } catch (err) {
    console.warn('Formspree backup send failed.', err);
    return false;
  }

  return formspreeResponse.ok;
}

function openMailClient(payload) {
  const subject = encodeURIComponent(payload.subject);
  const body = encodeURIComponent(payload.bodyText);
  window.location.href = `mailto:${FORM_RECIPIENT}?subject=${subject}&body=${body}`;
}

// ====== Toast 提示 ======
function showToast(message, type = 'info') {
  const existing = document.querySelector('.toast');
  if (existing) existing.remove();

  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;

  const icon = document.createElement('i');
  icon.className = type === 'error' ? 'fas fa-exclamation-circle' : 'fas fa-info-circle';

  const title = document.createElement('h4');
  title.textContent = type === 'error' ? '提示' : '请注意';

  const text = document.createElement('p');
  text.textContent = message;

  toast.append(icon, title, text);
  document.body.appendChild(toast);

  requestAnimationFrame(() => {
    toast.classList.add('show');
  });

  setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => toast.remove(), 400);
  }, 3600);
}

function showSuccessToast() {
  const existing = document.querySelector('.toast');
  if (existing) existing.remove();

  const toast = document.createElement('div');
  toast.className = 'toast toast-success';
  toast.innerHTML = '<i class="fas fa-check-circle"></i><h4>提交成功！</h4><p>预约信息已发送，红娘老师将在24小时内与您联系。</p>';
  document.body.appendChild(toast);

  requestAnimationFrame(() => {
    toast.classList.add('show');
  });

  setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => toast.remove(), 400);
  }, 4200);
}

// ====== 页面加载动画 ======
document.addEventListener('DOMContentLoaded', () => {
  const cards = document.querySelectorAll('.feature-card, .service-card, .case-card, .service-detail-card, .case-detail-card, .event-card, .pricing-card, .trust-card, .msg-tip');
  const cardObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
        }, index * 80);
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
