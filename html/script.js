const blogPosts = [
  { title: "My First Blog Post", author: "John Doe", content: "This is my first blog post!" },
  { title: "My Second Blog Post", author: "Jane Smith", content: "This is my second blog post!" },
  { title: "My Third Blog Post", author: "Bob Johnson", content: "This is my third blog post!" }
];

const blogPostList = document.getElementById("blog-posts");

for (let i = 0; i < blogPosts.length; i++) {
  const blogPost = blogPosts[i];

  const li = document.createElement("li");
  const h2 = document.createElement("h2");
  const h4 = document.createElement("h4");
  const p = document.createElement("p");

  h2.innerText = blogPost.title;
  h4.innerText = "By " + blogPost.author;
  p.innerText = blogPost.content;

  li.appendChild(h2);
  li.appendChild(h4);
  li.appendChild(p);

  blogPostList.appendChild(li);
}


// 获取导航栏和博客内容元素
const navbar = document.querySelector('#navbar');
const content = document.querySelector('#content');

// 导航栏链接点击事件
navbar.addEventListener('click', (event) => {
  // 阻止默认行为
  event.preventDefault();

  // 获取被点击的链接元素
  const link = event.target;

  // 如果被点击的元素不是链接，则直接返回
  if (link.tagName !== 'A') {
    return;
  }

  // 获取链接的href属性值，即要显示的博客内容
  const blogContent = link.getAttribute('href');

  // 遍历所有博客内容元素，隐藏除了要显示的内容外的其它元素
  for (let i = 0; i < content.children.length; i++) {
    const item = content.children[i];
    if (item.getAttribute('id') === blogContent) {
      item.style.display = 'block';
    } else {
      item.style.display = 'none';
    }
  }

  // 移除当前活动链接的active类，并给被点击的链接添加active类
  const activeLink = navbar.querySelector('.active');
  activeLink.classList.remove('active');
  link.classList.add('active');
});
