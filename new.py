print("hello")<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Developer Portfolio</title>
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700&display=swap&quot; rel="stylesheet">
    <style>
        :root {
            --primary: #2d89ef;
            --accent: #ffb900;
            --bg: #f4f6fb;
            --card-bg: #fff;
            --text: #222;
            --shadow: 0 4px 24px rgba(0,0,0,0.08);
        }
        * {
            box-sizing: border-box;
        }
        body {
            margin: 0;
            font-family: 'Montserrat', sans-serif;
            background: var(--bg);
            color: var(--text);
        }
        header {
            background: var(--primary);
            color: #fff;
            padding: 2rem 0 1rem 0;
            text-align: center;
            box-shadow: var(--shadow);
        }
        header h1 {
            margin: 0;
            font-size: 2.5rem;
            letter-spacing: 2px;
        }
        header p {
            margin: 0.5rem 0 0 0;
            font-size: 1.2rem;
            font-weight: 400;
        }
        nav {
            margin-top: 1rem;
        }
        nav a {
            color: #fff;
            text-decoration: none;
            margin: 0 1rem;
            font-weight: 700;
            transition: color 0.2s;
        }
        nav a:hover {
            color: var(--accent);
        }
        .container {
            max-width: 1100px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        .section-title {
            font-size: 2rem;
            margin-bottom: 1rem;
            color: var(--primary);
            text-align: center;
            letter-spacing: 1px;
        }
        .about {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            background: var(--card-bg);
            box-shadow: var(--shadow);
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 2rem;
        }
        .about-img {
            flex: 1 1 180px;
            max-width: 180px;
            margin-right: 2rem;
            border-radius: 50%;
            overflow: hidden;
            box-shadow: 0 2px 12px rgba(45,137,239,0.15);
        }
        .about-img img {
            width: 100%;
            display: block;
        }
        .about-text {
            flex: 2 1 300px;
        }
        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            justify-content: center;
            margin-bottom: 2rem;
        }
        .skill-card {
            background: var(--card-bg);
            box-shadow: var(--shadow);
            border-radius: 8px;
            padding: 1rem 2rem;
            min-width: 120px;
            text-align: center;
            font-weight: 700;
            color: var(--primary);
            transition: transform 0.2s;
        }
        .skill-card:hover {
            transform: translateY(-5px) scale(1.05);
            background: var(--accent);
            color: #fff;
        }
        .projects {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }
        .project-card {
            background: var(--card-bg);
            box-shadow: var(--shadow);
            border-radius: 10px;
            overflow: hidden;
            transition: transform 0.2s;
            display: flex;
            flex-direction: column;
        }
        .project-card:hover {
            transform: translateY(-5px) scale(1.03);
            box-shadow: 0 8px 32px rgba(45,137,239,0.15);
        }
        .project-img {
            width: 100%;
            height: 160px;
            object-fit: cover;
            background: #eee;
        }
        .project-content {
            padding: 1rem;
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .project-title {
            font-size: 1.2rem;
            color: var(--primary);
            margin: 0 0 0.5rem 0;
        }
        .project-desc {
            font-size: 1rem;
            margin-bottom: 1rem;
            color: #444;
        }
        .project-link {
            align-self: flex-end;
            text-decoration: none;
            color: var(--accent);
            font-weight: 700;
            transition: color 0.2s;
        }
        .project-link:hover {
            color: var(--primary);
        }
        footer {
            background: var(--primary);
            color: #fff;
            text-align: center;
            padding: 1.5rem 0;
            margin-top: 2rem;
            font-size: 1rem;
            letter-spacing: 1px;
        }
        @media (max-width: 700px) {
            .about {
                flex-direction: column;
                text-align: center;
            }
            .about-img {
                margin: 0 0 1rem 0;
            }
            .skills {
                flex-direction: column;
                align-items: center;
            }
            .container {
                padding: 0 0.5rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Jane Doe</h1>
        <p>Full Stack Developer & UI Enthusiast</p>
        <nav>
            <a href="#about">About</a>
            <a href="#skills">Skills</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </nav>
    </header>
    <div class="container">
        <section id="about" class="about">
            <div class="about-img">
                <img src="https://randomuser.me/api/portraits/women/44.jpg&quot; alt="Jane Doe">
            </div>
            <div class="about-text">
                <h2 class="section-title">About Me</h2>
                <p>
                    Hi! I'm Jane, a passionate developer crafting modern web experiences. I love building scalable apps, designing beautiful interfaces, and solving real-world problems with code. Let's create something amazing together!
                </p>
            </div>
        </section>
        <section id="skills">
            <h2 class="section-title">Skills</h2>
            <div class="skills">
                <div class="skill-card">HTML5</div>
                <div class="skill-card">CSS3</div>
                <div class="skill-card">JavaScript</div>
                <div class="skill-card">React</div>
                <div class="skill-card">Node.js</div>
                <div class="skill-card">MongoDB</div>
                <div class="skill-card">Git & GitHub</div>
                <div class="skill-card">UI/UX Design</div>
            </div>
        </section>
        <section id="projects">
            <h2 class="section-title">Projects</h2>
            <div class="projects">
                <div class="project-card">
                    <img class="project-img" src="https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=400&q=80&quot; alt="Project 1">
                    <div class="project-content">
                        <div>
                            <div class="project-title">Portfolio Website</div>
                            <div class="project-desc">A personal portfolio site built with React and styled-components, featuring responsive design and smooth animations.</div>
                        </div>
                        <a class="project-link" href="#" target="_blank">View Project</a>
                    </div>
                </div>
                <div class="project-card">
                    <img class="project-img" src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&q=80&quot; alt="Project 2">
                    <div class="project-content">
                        <div>
                            <div class="project-title">Task Manager App</div>
                            <div class="project-desc">A full-stack MERN app for managing tasks, with authentication, real-time updates, and a clean UI.</div>
                        </div>
                        <a class="project-link" href="#" target="_blank">View Project</a>
                    </div>
                </div>
                <div class="project-card">
                    <img class="project-img" src="https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=400&q=80&quot; alt="Project 3">
                    <div class="project-content">
                        <div>
                            <div class="project-title">Weather Dashboard</div>
                            <div class="project-desc">A responsive dashboard that fetches live weather data using APIs, with charts and location search.</div>
                        </div>
                        <a class="project-link" href="#" target="_blank">View Project</a>
                    </div>
                </div>
            </div>
        </section>
        <section id="contact">
            <h2 class="section-title">Contact</h2>
            <form style="background:var(--card-bg);box-shadow:var(--shadow);border-radius:8px;padding:2rem;max-width:500px;margin:0 auto;">
                <div style="margin-bottom:1rem;">
                    <input type="text" placeholder="Your Name" required style="width:100%;padding:0.7rem;border-radius:4px;border:1px solid #ddd;">
                </div>
                <div style="margin-bottom:1rem;">
                    <input type="email" placeholder="Your Email" required style="width:100%;padding:0.7rem;border-radius:4px;border:1px solid #ddd;">
                </div>
                <div style="margin-bottom:1rem;">
                    <textarea placeholder="Your Message" required style="width:100%;padding:0.7rem;border-radius:4px;border:1px solid #ddd;min-height:80px;"></textarea>
                </div>
                <button type="submit" style="background:var(--primary);color:#fff;padding:0.7rem 2rem;border:none;border-radius:4px;font-weight:700;cursor:pointer;transition:background 0.2s;">Send</button>
            </form>
        </section>
    </div>
    <footer>
        &copy; 2024 Jane Doe. All rights reserved.
    </footer>
</body>
</html></div><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>All HTML Tags Example</title>
    <meta name="viewport" content="widtvv vh=device-width, initial-scale=1.0">
    <style>
        body { font-family: Arial, sans-serif; }
    </style>
    <script>
        function showAlert() {
            alert('Hello from script!');
        }
    </script>
</head>
<body>
    <header>
        <h1>Main Heading</h1>
        <nav>
            <ul>
                <li><a href="#section1">Section 1</a></li>
                <li><a href="#section2">Section 2</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="section1">
            <h2>Section 1</h2>
            <article>
                <h3>Article Title</h3>
                <p>This is a <strong>paragraph</strong> with <em>emphasis</em> and <mark>highlight</mark>.</p>
                <blockquote cite="https://example.com">This is a blockquote.</blockquote>
                <pre>
function hello() {
    console.log("Hello World");
}
                </pre>
                <code>console.log('Inline code');</code>
                <br>
                <hr>
                <ul>
                    <li>Unordered list item</li>
                </ul>
                <ol>
                    <li>Ordered list item</li>
                </ol>
                <dl>
                    <dt>Term</dt>
                    <dd>Definition</dd>
                </dl>
                <figure>
                    <img src="https://via.placeholder.com/150&quot; alt="Placeholder Image">
                    <figcaption>Sample Image</figcaption>
                </figure>
                <table border="1">
                    <caption>Sample Table</caption>
                    <thead>
                        <tr>
                            <th>Header 1</th>
                            <th>Header 2</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Cell 1</td>
                            <td>Cell 2</td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr>
                            <td colspan="2">Footer</td>
                        </tr>
                    </tfoot>
                </table>
                <form>
                    <fieldset>
                        <legend>Form Example</legend>
                        <label for="name">Name:</label>
                        <input type="text" id="name" name="name">
                        <input type="checkbox" id="subscribe" name="subscribe">
                        <label for="subscribe">Subscribe</label>
                        <input type="radio" id="male" name="gender" value="male">
                        <label for="male">Male</label>
                        <input type="radio" id="female" name="gender" value="female">
                        <label for="female">Female</label>
                        <select name="country">
                            <option value="us">USA</option>
                            <option value="uk">UK</option>
                        </select>
                        <textarea name="comments"></textarea>
                        <button type="button" onclick="showAlert()">Click Me</button>
                        <input type="submit" value="Submit">
                    </fieldset>
                </form>
                <details>
                    <summary>More Info</summary>
                    <p>Hidden details shown here.</p>
                </details>
                <progress value="50" max="100"></progress>
                <meter value="0.6">60%</meter>
                <time datetime="2024-06-01">June 1, 2024</time>
                <abbr title="HyperText Markup Language">HTML</abbr>
                <address>
                    123 Main St, City, Country
                </address>
                <bdo dir="rtl">Right to left text</bdo>
                <sup>Superscript</sup>
                <sub>Subscript</sub>
                <small>Small text</small>
                <s>Strikethrough</s>
                <u>Underlined</u>
                <i>Italic</i>
                <b>Bold</b>
                <span>Span text</span>
            </article>
        </section>
        <section id="section2">
            <h2>Section 2</h2>
            <aside>
                <p>This is an aside.</p>
            </aside>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 Example Footer</p>
    </footer>
</body>
</html>
