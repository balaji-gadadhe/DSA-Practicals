
## Practical 1 – Student Portfolio Page (HTML Text Formatting + Form Elements)

```html
<!DOCTYPE html>
<html>
<head><title>Student Portfolio</title></head>
<body>
  <h1><b>Balaji Deshmukh</b></h1>
  <p><i>Course:</i> <u>B.Tech Computer Science Engineering</u></p>
  <p><big>Hobbies:</big></p>

  <form>
    <b>Select Hobbies:</b><br>
    <input type="checkbox" checked> Photography<br>
    <input type="checkbox" checked> Gaming<br>
    <input type="checkbox"> Reading<br><br>

    <b>Gender:</b><br>
    <input type="radio" name="gender"> Male
    <input type="radio" name="gender"> Female<br><br>

    <b>Name:</b> <input type="text" value="Balaji"><br><br>
    <input type="submit" value="Submit">
  </form>
</body>
</html>
```

---

## Practical 2 – Survey Form (HTML + CSS)

```html
<!DOCTYPE html>
<html>
<head>
<title>Survey Form</title>
<style>
  body { font-family: Arial; background: #f0f0f0; }
  form { background: white; padding: 20px; width: 400px; margin: auto; border-radius: 8px; }
  input, select { margin: 8px 0; padding: 5px; width: 100%; }
  button { background: blue; color: white; padding: 8px 20px; border: none; cursor: pointer; }
</style>
</head>
<body>
  <form>
    <h2>Survey Form</h2>
    <label>Name:</label>
    <input type="text" placeholder="Your name"><br>

    <label>Email:</label>
    <input type="email" placeholder="Your email"><br>

    <label>Age Group:</label><br>
    <input type="radio" name="age"> 18-25
    <input type="radio" name="age"> 26-35<br><br>

    <label>Interests:</label><br>
    <input type="checkbox"> Technology
    <input type="checkbox"> Sports
    <input type="checkbox"> Music<br><br>

    <label>Comments:</label><br>
    <textarea rows="3" cols="40"></textarea><br><br>

    <button type="submit">Submit</button>
  </form>
</body>
</html>
```

---

## Practical 3 – Restaurant Website (HTML + CSS Grid)

```html
<!DOCTYPE html>
<html>
<head>
<title>The Spice Garden</title>
<style>
  body { font-family: Arial; margin: 0; background: #fff8f0; }
  header { background: #8B0000; color: white; text-align: center; padding: 20px; }
  nav a { color: white; margin: 0 15px; text-decoration: none; }
  .menu-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    padding: 30px;
  }
  .card { background: white; border: 1px solid #ddd; padding: 15px; border-radius: 8px; text-align: center; }
  .card img { width: 100%; height: 150px; object-fit: cover; border-radius: 5px; }
  footer { background: #8B0000; color: white; text-align: center; padding: 10px; }
</style>
</head>
<body>
  <header>
    <h1>🍽 The Spice Garden</h1>
    <nav>
      <a href="#">Home</a>
      <a href="#">Menu</a>
      <a href="#">Gallery</a>
      <a href="#">Contact</a>
    </nav>
  </header>

  <h2 style="text-align:center">Our Menu</h2>
  <div class="menu-grid">
    <div class="card">
      <img src="https://via.placeholder.com/200x150?text=Burger" alt="Burger">
      <h3>Burger</h3>
      <p>₹120</p>
    </div>
    <div class="card">
      <img src="https://via.placeholder.com/200x150?text=Pizza" alt="Pizza">
      <h3>Pizza</h3>
      <p>₹250</p>
    </div>
    <div class="card">
      <img src="https://via.placeholder.com/200x150?text=Pasta" alt="Pasta">
      <h3>Pasta</h3>
      <p>₹180</p>
    </div>
  </div>

  <footer><p>© 2025 The Spice Garden</p></footer>
</body>
</html>
```

---

## Practical 4 – I2IT College Website Page (HTML + CSS)

```html
<!DOCTYPE html>
<html>
<head>
<title>I2IT College</title>
<style>
  body { font-family: Arial; background: #eef4ff; }
  header { background: #003080; color: white; padding: 20px; text-align: center; }
  table { border-collapse: collapse; margin: 20px auto; width: 80%; }
  th { background: #003080; color: white; padding: 10px; }
  td { border: 1px solid #ccc; padding: 10px; text-align: center; }
  tr:nth-child(even) { background: #d0e4ff; }
</style>
</head>
<body>
  <header>
    <img src="https://via.placeholder.com/80?text=LOGO" alt="I2IT Logo">
    <h1>International Institute of Information Technology</h1>
    <p>Official Website: <a href="https://www.isquareit.edu.in" style="color:yellow">www.isquareit.edu.in</a></p>
  </header>

  <h2 style="text-align:center">Courses & Subjects</h2>
  <table>
    <tr><th>Course</th><th>Subject</th><th>Credits</th></tr>
    <tr><td>B.Tech CSE</td><td>Data Structures</td><td>4</td></tr>
    <tr><td>B.Tech CSE</td><td>Web Development Lab</td><td>2</td></tr>
    <tr><td>B.Tech CSE</td><td>Discrete Mathematics</td><td>3</td></tr>
    <tr><td>B.Tech CSE</td><td>Database Management</td><td>4</td></tr>
  </table>
</body>
</html>
```

---

## Practical 5 – Student Registration Form

```html
<!DOCTYPE html>
<html>
<head>
<title>Student Registration</title>
<style>
  body { font-family: Arial; background: #f5f5f5; }
  form { background: white; width: 350px; margin: 30px auto; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px #ccc; }
  input, select { width: 100%; padding: 8px; margin: 8px 0 16px; box-sizing: border-box; }
  button { background: #003080; color: white; padding: 10px 20px; border: none; cursor: pointer; width: 100%; }
</style>
</head>
<body>
  <form>
    <h2>Student Registration</h2>

    <label>Name:</label>
    <input type="text" placeholder="Full Name" required>

    <label>Email:</label>
    <input type="email" placeholder="Email Address" required>

    <label>Gender:</label><br>
    <input type="radio" name="gender"> Male
    <input type="radio" name="gender"> Female<br><br>

    <label>Date of Birth:</label>
    <input type="date" required>

    <button type="submit">Register</button>
  </form>
</body>
</html>
```

---

## Practical 6 – I2IT TechCon 2025 Event Page

```html
<!DOCTYPE html>
<html>
<head>
<title>I2IT TechCon 2025</title>
<style>
  body { font-family: Arial; margin: 0; }
  header { background: #1a1a2e; color: white; text-align: center; padding: 30px; }
  nav { background: #16213e; padding: 10px; text-align: center; }
  nav a { color: white; margin: 0 15px; text-decoration: none; }
  section { padding: 20px 40px; }
  table { border-collapse: collapse; width: 100%; }
  th { background: #1a1a2e; color: white; padding: 10px; }
  td { border: 1px solid #ccc; padding: 10px; }
  input, textarea { width: 100%; padding: 8px; margin: 5px 0 15px; }
  button { background: #e94560; color: white; padding: 10px 20px; border: none; }
</style>
</head>
<body>

<header>
  <h1>🚀 I2IT TechCon 2025</h1>
  <p>Annual Technology Conference – Hinjewadi, Pune</p>
</header>

<nav>
  <a href="#about">About</a>
  <a href="#schedule">Schedule</a>
  <a href="#contact">Contact</a>
</nav>

<section id="about">
  <h2>About</h2>
  <p>I2IT TechCon 2025 is a flagship tech event featuring talks, workshops, and project expos by industry leaders and students.</p>
</section>

<section id="schedule">
  <h2>Schedule</h2>
  <table>
    <tr><th>Time</th><th>Event</th><th>Speaker</th></tr>
    <tr><td>10:00 AM</td><td>Inauguration</td><td>Principal</td></tr>
    <tr><td>11:00 AM</td><td>AI & ML Talk</td><td>Dr. Sharma</td></tr>
    <tr><td>1:00 PM</td><td>Web Dev Workshop</td><td>Mr. Joshi</td></tr>
    <tr><td>3:00 PM</td><td>Project Expo</td><td>Students</td></tr>
  </table>
</section>

<section id="contact">
  <h2>Contact Us</h2>
  <form>
    <label>Name:</label>
    <input type="text" placeholder="Your name">
    <label>Email:</label>
    <input type="email" placeholder="Your email">
    <label>Message:</label>
    <textarea rows="4" placeholder="Your message"></textarea>
    <button type="submit">Send</button>
  </form>
</section>

</body>
</html>
```

---

## Practical 7 – Student Result Dashboard (Inline + Internal + External CSS)

> Save the external CSS as `style.css` in the same folder.

**style.css**
```css
body {
  font-family: Arial;
  background: #f0f4ff;
}
h1 {
  text-align: center;
  color: #003080;
}
```

**result.html**
```html
<!DOCTYPE html>
<html>
<head>
<title>Result Dashboard</title>
<link rel="stylesheet" href="style.css">
<style>
  /* Internal CSS – table styling */
  table { border-collapse: collapse; width: 60%; margin: 20px auto; }
  th { background: #003080; color: white; padding: 10px; }
  td { border: 1px solid #aaa; padding: 10px; text-align: center; }
</style>
</head>
<body>

<h1>Student Result Dashboard</h1>
<h3 style="text-align:center">Student: Balaji Deshmukh | Roll: SCA54</h3>

<table>
  <tr><th>Subject</th><th>Marks (/100)</th><th>Grade</th></tr>
  <tr><td>Maths</td><td style="color:green; font-weight:bold">92</td><td>A+</td></tr><!-- Inline CSS: top scorer -->
  <tr><td>Physics</td><td>78</td><td>A</td></tr>
  <tr><td>Chemistry</td><td>65</td><td>B</td></tr>
  <tr><td>CS</td><td>88</td><td>A</td></tr>
  <tr><td>English</td><td>70</td><td>B+</td></tr>
</table>

</body>
</html>
```

---

## Practical 8 – Bootstrap Responsive College Homepage

```html
<!DOCTYPE html>
<html>
<head>
<title>College Homepage</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

<nav class="navbar navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="#">I2IT College</a>
  </div>
</nav>

<div class="container mt-4">
  <div class="jumbotron bg-primary text-white p-5 rounded mb-4">
    <h1>Welcome to I2IT</h1>
    <p>Excellence in Technology Education</p>
    <a href="#" class="btn btn-light">Know More</a>
  </div>

  <div class="row">
    <div class="col-md-4 mb-3">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">About Us</h5>
          <p class="card-text">I2IT is a premier engineering institute located in Hinjewadi, Pune.</p>
        </div>
      </div>
    </div>
    <div class="col-md-4 mb-3">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Courses</h5>
          <p class="card-text">B.Tech, M.Tech programs in CS, IT, ENTC and more.</p>
        </div>
      </div>
    </div>
    <div class="col-md-4 mb-3">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Contact</h5>
          <p class="card-text">Hinjewadi, Pune – 411057 | info@isquareit.edu.in</p>
        </div>
      </div>
    </div>
  </div>
</div>

<footer class="bg-dark text-white text-center p-3 mt-4">© 2025 I2IT</footer>

</body>
</html>
```

---

## Practical 9 – Library Signup Form Validation (JavaScript)

```html
<!DOCTYPE html>
<html>
<head><title>Library Signup</title>
<style>
  form { width: 350px; margin: 30px auto; font-family: Arial; }
  input { width: 100%; padding: 8px; margin: 8px 0 5px; box-sizing: border-box; }
  .err { color: red; font-size: 12px; }
  button { background: #003080; color: white; padding: 10px; width: 100%; border: none; cursor: pointer; }
</style>
</head>
<body>
<form onsubmit="return validate()">
  <h2>Library Signup</h2>

  Name: <input type="text" id="name">
  <div class="err" id="nameErr"></div>

  Email: <input type="text" id="email">
  <div class="err" id="emailErr"></div>

  Mobile: <input type="text" id="mobile">
  <div class="err" id="mobileErr"></div>

  <button type="submit">Register</button>
</form>

<script>
function validate() {
  let valid = true;

  document.getElementById('nameErr').innerText = '';
  document.getElementById('emailErr').innerText = '';
  document.getElementById('mobileErr').innerText = '';

  let name = document.getElementById('name').value.trim();
  let email = document.getElementById('email').value.trim();
  let mobile = document.getElementById('mobile').value.trim();

  if (name === '') {
    document.getElementById('nameErr').innerText = 'Name is required.';
    valid = false;
  }

  let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    document.getElementById('emailErr').innerText = 'Enter a valid email.';
    valid = false;
  }

  let mobileRegex = /^[6-9]\d{9}$/;
  if (!mobileRegex.test(mobile)) {
    document.getElementById('mobileErr').innerText = 'Enter valid 10-digit mobile number.';
    valid = false;
  }

  if (valid) alert('Registration Successful!');
  return false;
}
</script>
</body>
</html>
```

---

## Practical 10 – Dynamic Content Using DOM (JavaScript)

```html
<!DOCTYPE html>
<html>
<head><title>DOM Dynamic Content</title>
<style>
  body { font-family: Arial; text-align: center; padding: 30px; }
  #output { margin-top: 20px; padding: 15px; background: #eef; border-radius: 8px; }
  button { margin: 5px; padding: 10px 20px; cursor: pointer; }
</style>
</head>
<body>
  <h2>Dynamic Content with DOM</h2>
  <button onclick="changeText()">Change Text</button>
  <button onclick="changeColor()">Change Color</button>
  <button onclick="addItem()">Add List Item</button>

  <div id="output">
    <p id="msg">Hello! Click buttons to change content.</p>
    <ul id="myList"></ul>
  </div>

<script>
  let count = 1;

  function changeText() {
    document.getElementById('msg').innerText = 'Text changed dynamically! Count: ' + count++;
  }

  function changeColor() {
    let colors = ['#ffcccc', '#ccffcc', '#ccccff', '#ffffcc'];
    document.getElementById('output').style.background = colors[count % colors.length];
    count++;
  }

  function addItem() {
    let li = document.createElement('li');
    li.innerText = 'Item ' + count++;
    document.getElementById('myList').appendChild(li);
  }
</script>
</body>
</html>
```

---

## Practical 11 – Simple Calculator (JavaScript + switch-case)

```html
<!DOCTYPE html>
<html>
<head><title>Calculator</title>
<style>
  body { font-family: Arial; display: flex; justify-content: center; padding: 30px; }
  .calc { background: #222; padding: 20px; border-radius: 10px; width: 250px; }
  input { width: 100%; padding: 10px; font-size: 18px; text-align: right; margin-bottom: 10px; box-sizing: border-box; }
  .btns { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; }
  button { padding: 12px; font-size: 16px; cursor: pointer; border-radius: 5px; border: none; background: #444; color: white; }
  button.op { background: #ff9500; }
  button.eq { background: #00b300; }
  button.cl { background: #cc0000; }
</style>
</head>
<body>
<div class="calc">
  <input type="text" id="display" readonly value="0">
  <div class="btns">
    <button class="cl" onclick="clearDisp()">C</button>
    <button onclick="appendVal('(')">(</button>
    <button onclick="appendVal(')')">)</button>
    <button class="op" onclick="appendVal('/')">÷</button>

    <button onclick="appendVal('7')">7</button>
    <button onclick="appendVal('8')">8</button>
    <button onclick="appendVal('9')">9</button>
    <button class="op" onclick="appendVal('*')">×</button>

    <button onclick="appendVal('4')">4</button>
    <button onclick="appendVal('5')">5</button>
    <button onclick="appendVal('6')">6</button>
    <button class="op" onclick="appendVal('-')">−</button>

    <button onclick="appendVal('1')">1</button>
    <button onclick="appendVal('2')">2</button>
    <button onclick="appendVal('3')">3</button>
    <button class="op" onclick="appendVal('+')">+</button>

    <button onclick="appendVal('0')">0</button>
    <button onclick="appendVal('.')">.</button>
    <button onclick="deleteLast()">⌫</button>
    <button class="eq" onclick="calculate()">=</button>
  </div>
</div>

<script>
  let disp = document.getElementById('display');

  function appendVal(val) {
    if (disp.value === '0') disp.value = val;
    else disp.value += val;
  }

  function clearDisp() { disp.value = '0'; }

  function deleteLast() {
    disp.value = disp.value.length > 1 ? disp.value.slice(0, -1) : '0';
  }

  function calculate() {
    try { disp.value = eval(disp.value); }
    catch { disp.value = 'Error'; }
  }
</script>
</body>
</html>
```

---

## Practical 12 – PHP Dashboard Greeting Page

```php
<?php
  $hour = date('H');
  if ($hour < 12) $greeting = "Good Morning";
  elseif ($hour < 17) $greeting = "Good Afternoon";
  else $greeting = "Good Evening";

  $datetime = date('l, d F Y – h:i:s A');
?>
<!DOCTYPE html>
<html>
<head><title>Dashboard</title>
<style>
  body { font-family: Arial; background: #eef4ff; display: flex; justify-content: center; align-items: center; height: 100vh; }
  .box { background: white; padding: 40px; border-radius: 12px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
  h1 { color: #003080; }
  p { color: #555; font-size: 18px; }
</style>
</head>
<body>
  <div class="box">
    <h1>👋 <?= $greeting ?>, Welcome to Dashboard!</h1>
    <p>📅 <?= $datetime ?></p>
  </div>
</body>
</html>
```

---

## Practical 13 – PHP Project Competition Registration Form (POST)

**form.html**
```html
<!DOCTYPE html>
<html>
<head><title>Project Registration</title></head>
<body>
  <h2>Project Competition Registration</h2>
  <form action="process.php" method="POST">
    Name: <input type="text" name="name"><br><br>
    Email: <input type="email" name="email"><br><br>
    Project Title: <input type="text" name="project"><br><br>
    Team Size: <input type="number" name="team"><br><br>
    <input type="submit" value="Register">
  </form>
</body>
</html>
```

**process.php**
```php
<?php
  $name = $_POST['name'];
  $email = $_POST['email'];
  $project = $_POST['project'];
  $team = $_POST['team'];
?>
<!DOCTYPE html>
<html>
<body>
  <h2>Registration Successful!</h2>
  <p><b>Name:</b> <?= $name ?></p>
  <p><b>Email:</b> <?= $email ?></p>
  <p><b>Project:</b> <?= $project ?></p>
  <p><b>Team Size:</b> <?= $team ?></p>
  <a href="form.html">Go Back</a>
</body>
</html>
```

---

## Practical 14 – PHP String Manipulation (reverse, length, substring)

```php
<?php
  $str = "Hello World";
  $reversed = strrev($str);
  $length = strlen($str);
  $substr = substr($str, 6, 5);
?>
<!DOCTYPE html>
<html>
<body>
  <h2>PHP String Manipulation</h2>
  <p><b>Original:</b> <?= $str ?></p>
  <p><b>Reversed:</b> <?= $reversed ?></p>
  <p><b>Length:</b> <?= $length ?></p>
  <p><b>Substring (pos 6, len 5):</b> <?= $substr ?></p>
</body>
</html>
```

---

## Practical 15 – PHP Subject Marks Array (Max Marks + Percentage)

```php
<?php
  $marks = [85, 90, 78, 92, 88];
  $subjects = ["Maths", "Physics", "Chemistry", "CS", "English"];
  $max = max($marks);
  $total = array_sum($marks);
  $percentage = ($total / (count($marks) * 100)) * 100;
?>
<!DOCTYPE html>
<html>
<body>
  <h2>Student Marks Summary</h2>
  <table border="1" cellpadding="8">
    <tr><th>Subject</th><th>Marks</th></tr>
    <?php for ($i = 0; $i < count($marks); $i++): ?>
    <tr><td><?= $subjects[$i] ?></td><td><?= $marks[$i] ?></td></tr>
    <?php endfor; ?>
  </table>
  <p><b>Maximum Marks:</b> <?= $max ?></p>
  <p><b>Total:</b> <?= $total ?> / <?= count($marks)*100 ?></p>
  <p><b>Percentage:</b> <?= $percentage ?>%</p>
</body>
</html>
```

---

## Practical 16 – Area Calculator (JavaScript + switch-case)

```html
<!DOCTYPE html>
<html>
<head><title>Area Calculator</title>
<style>
  body { font-family: Arial; padding: 30px; }
  input, select { padding: 8px; margin: 8px; }
  button { padding: 10px 20px; background: #003080; color: white; border: none; cursor: pointer; }
  #result { margin-top: 15px; font-size: 20px; color: green; }
</style>
</head>
<body>
  <h2>Area Calculator</h2>
  <label>Shape:
    <select id="shape" onchange="updateFields()">
      <option value="rectangle">Rectangle</option>
      <option value="triangle">Triangle</option>
      <option value="circle">Circle</option>
    </select>
  </label><br>

  <div id="inputs">
    <input type="number" id="val1" placeholder="Length">
    <input type="number" id="val2" placeholder="Width">
  </div>

  <button onclick="calcArea()">Calculate Area</button>
  <div id="result"></div>

<script>
  function updateFields() {
    let shape = document.getElementById('shape').value;
    let html = '';
    switch(shape) {
      case 'rectangle': html = '<input type="number" id="val1" placeholder="Length"><input type="number" id="val2" placeholder="Width">'; break;
      case 'triangle':  html = '<input type="number" id="val1" placeholder="Base"><input type="number" id="val2" placeholder="Height">'; break;
      case 'circle':    html = '<input type="number" id="val1" placeholder="Radius">'; break;
    }
    document.getElementById('inputs').innerHTML = html;
  }

  function calcArea() {
    let shape = document.getElementById('shape').value;
    let v1 = parseFloat(document.getElementById('val1').value);
    let v2 = document.getElementById('val2') ? parseFloat(document.getElementById('val2').value) : 0;
    let area;

    switch(shape) {
      case 'rectangle': area = v1 * v2; break;
      case 'triangle':  area = 0.5 * v1 * v2; break;
      case 'circle':    area = Math.PI * v1 * v1; break;
    }

    document.getElementById('result').innerText = 'Area = ' + area.toFixed(2);
  }
</script>
</body>
</html>
```

---

## Practical 17 – PHP Student Marks Form (POST + String + Array)

**marks_form.html**
```html
<!DOCTYPE html>
<html>
<body>
  <h2>Student Marks Entry</h2>
  <form action="marks_process.php" method="POST">
    Student Name: <input type="text" name="name"><br><br>
    Subject 1: <input type="number" name="m1"><br>
    Subject 2: <input type="number" name="m2"><br>
    Subject 3: <input type="number" name="m3"><br>
    Subject 4: <input type="number" name="m4"><br>
    Subject 5: <input type="number" name="m5"><br><br>
    <input type="submit" value="Calculate">
  </form>
</body>
</html>
```

**marks_process.php**
```php
<?php
  $name = ucwords(strtolower($_POST['name']));
  $marks = [$_POST['m1'], $_POST['m2'], $_POST['m3'], $_POST['m4'], $_POST['m5']];
  $total = array_sum($marks);
  $average = $total / count($marks);
?>
<!DOCTYPE html>
<html>
<body>
  <h2>Result for: <?= $name ?></h2>
  <p>Name (formatted): <?= $name ?></p>
  <p>Name Length: <?= strlen($name) ?></p>
  <p>Total Marks: <?= $total ?> / 500</p>
  <p>Average: <?= number_format($average, 2) ?></p>
</body>
</html>
```

---

## Practical 18 – PHP Search Roll Number in Array

```php
<?php
  $rolls = [101, 102, 103, 104, 105];
  $search = isset($_GET['roll']) ? intval($_GET['roll']) : null;
  $found = $search !== null ? in_array($search, $rolls) : null;
?>
<!DOCTYPE html>
<html>
<body>
  <h2>Search Student Roll Number</h2>
  <form method="GET">
    Enter Roll No: <input type="number" name="roll">
    <button type="submit">Search</button>
  </form>

  <?php if ($found === true): ?>
    <p style="color:green">✅ Roll No <?= $search ?> FOUND in records.</p>
  <?php elseif ($found === false): ?>
    <p style="color:red">❌ Roll No <?= $search ?> NOT found.</p>
  <?php endif; ?>
</body>
</html>
```

---

## Practical 19 – PHP String Operations (All Types)

```php
<?php
  $str = "000056.8";
  $normal = "hello world php";
?>
<!DOCTYPE html>
<html>
<body>
  <h2>PHP String Operations</h2>

  <p><b>a) Uppercase:</b> <?= strtoupper($normal) ?></p>
  <p><b>b) Lowercase:</b> <?= strtolower("HELLO WORLD PHP") ?></p>
  <p><b>c) First char uppercase:</b> <?= ucfirst($normal) ?></p>
  <p><b>d) All words first char uppercase:</b> <?= ucwords($normal) ?></p>
  <p><b>e) Remove leading zeroes (<?= $str ?>):</b> <?= ltrim($str, '0') ?></p>
  <p><b>f) Reverse:</b> <?= strrev($normal) ?></p>
  <p><b>f) Length:</b> <?= strlen($normal) ?></p>
  <p><b>f) Substring (pos 6, len 5):</b> <?= substr($normal, 6, 5) ?></p>
</body>
</html>
```

---

## Practical 21 – Student Registration Form with JS Validation + CSS

```html
<!DOCTYPE html>
<html>
<head><title>Registration Form</title>
<style>
  body { font-family: Arial; background: #f0f4ff; display: flex; justify-content: center; padding: 30px; }
  .form-box { background: white; padding: 30px; border-radius: 10px; width: 380px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
  input { width: 100%; padding: 9px; margin: 6px 0 4px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 5px; }
  .err { color: red; font-size: 12px; margin-bottom: 8px; }
  button { background: #003080; color: white; padding: 12px; width: 100%; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
  #success { color: green; font-weight: bold; margin-top: 15px; text-align: center; display: none; }
</style>
</head>
<body>
<div class="form-box">
  <h2>Student Registration</h2>

  Name: <input type="text" id="name">
  <div class="err" id="nameErr"></div>

  Email: <input type="email" id="email">
  <div class="err" id="emailErr"></div>

  Password: <input type="password" id="pwd">
  <div class="err" id="pwdErr"></div>

  Confirm Password: <input type="password" id="cpwd">
  <div class="err" id="cpwdErr"></div>

  Phone: <input type="text" id="phone">
  <div class="err" id="phoneErr"></div>

  <button onclick="validate()">Register</button>
  <div id="success">✅ Registration Successful!</div>
</div>

<script>
function validate() {
  let ok = true;
  const ids = ['name','email','pwd','cpwd','phone'];
  ids.forEach(id => document.getElementById(id+'Err').innerText = '');

  if (!document.getElementById('name').value.trim()) {
    document.getElementById('nameErr').innerText = 'Name required'; ok = false;
  }
  let email = document.getElementById('email').value;
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    document.getElementById('emailErr').innerText = 'Invalid email'; ok = false;
  }
  let pwd = document.getElementById('pwd').value;
  if (pwd.length < 6) {
    document.getElementById('pwdErr').innerText = 'Min 6 characters'; ok = false;
  }
  if (pwd !== document.getElementById('cpwd').value) {
    document.getElementById('cpwdErr').innerText = 'Passwords do not match'; ok = false;
  }
  if (!/^[6-9]\d{9}$/.test(document.getElementById('phone').value)) {
    document.getElementById('phoneErr').innerText = 'Invalid phone number'; ok = false;
  }

  if (ok) document.getElementById('success').style.display = 'block';
}
</script>
</body>
</html>
```

---

## Practical 22 – Simple Quiz Web Application (10 MCQs)

```html
<!DOCTYPE html>
<html>
<head><title>Simple Quiz</title>
<style>
  body { font-family: Arial; background: #f5f5f5; padding: 20px; }
  .quiz { background: white; padding: 20px; max-width: 600px; margin: auto; border-radius: 10px; box-shadow: 0 2px 10px #ccc; }
  .question { margin-bottom: 20px; }
  button { background: #003080; color: white; padding: 12px 30px; border: none; cursor: pointer; font-size: 16px; border-radius: 5px; }
  #result { font-size: 22px; color: green; margin-top: 20px; text-align: center; }
</style>
</head>
<body>
<div class="quiz">
  <h2>Simple Quiz</h2>
  <form id="quizForm">

    <div class="question"><b>1. What does HTML stand for?</b><br>
      <input type="radio" name="q1" value="a"> HyperText Markup Language<br>
      <input type="radio" name="q1" value="b"> High Text Machine Language<br>
      <input type="radio" name="q1" value="c"> HyperTransfer Markup Language
    </div>

    <div class="question"><b>2. Which tag is used for a hyperlink?</b><br>
      <input type="radio" name="q2" value="a"> &lt;link&gt;<br>
      <input type="radio" name="q2" value="b"> &lt;a&gt;<br>
      <input type="radio" name="q2" value="c"> &lt;href&gt;
    </div>

    <div class="question"><b>3. CSS stands for?</b><br>
      <input type="radio" name="q3" value="a"> Cascading Style Sheets<br>
      <input type="radio" name="q3" value="b"> Computer Style Sheets<br>
      <input type="radio" name="q3" value="c"> Creative Style System
    </div>

    <div class="question"><b>4. Which is a JavaScript framework?</b><br>
      <input type="radio" name="q4" value="a"> Django<br>
      <input type="radio" name="q4" value="b"> React<br>
      <input type="radio" name="q4" value="c"> Laravel
    </div>

    <div class="question"><b>5. PHP stands for?</b><br>
      <input type="radio" name="q5" value="a"> Personal Home Page<br>
      <input type="radio" name="q5" value="b"> PHP: Hypertext Preprocessor<br>
      <input type="radio" name="q5" value="c"> Pre Hypertext Processor
    </div>

    <div class="question"><b>6. Which tag creates a table row?</b><br>
      <input type="radio" name="q6" value="a"> &lt;td&gt;<br>
      <input type="radio" name="q6" value="b"> &lt;th&gt;<br>
      <input type="radio" name="q6" value="c"> &lt;tr&gt;
    </div>

    <div class="question"><b>7. Which method sends form data in URL?</b><br>
      <input type="radio" name="q7" value="a"> POST<br>
      <input type="radio" name="q7" value="b"> GET<br>
      <input type="radio" name="q7" value="c"> PUT
    </div>

    <div class="question"><b>8. DOM stands for?</b><br>
      <input type="radio" name="q8" value="a"> Document Object Model<br>
      <input type="radio" name="q8" value="b"> Data Object Method<br>
      <input type="radio" name="q8" value="c"> Document Open Method
    </div>

    <div class="question"><b>9. Bootstrap is a __ framework.</b><br>
      <input type="radio" name="q9" value="a"> Backend<br>
      <input type="radio" name="q9" value="b"> Frontend CSS<br>
      <input type="radio" name="q9" value="c"> Database
    </div>

    <div class="question"><b>10. Which is used to select element by ID in JS?</b><br>
      <input type="radio" name="q10" value="a"> document.getClass()<br>
      <input type="radio" name="q10" value="b"> document.getElementById()<br>
      <input type="radio" name="q10" value="c"> document.selectId()
    </div>

    <button type="button" onclick="submitQuiz()">Submit Quiz</button>
  </form>
  <div id="result"></div>
</div>

<script>
  const answers = { q1:'a', q2:'b', q3:'a', q4:'b', q5:'b', q6:'c', q7:'b', q8:'a', q9:'b', q10:'b' };

  function submitQuiz() {
    let score = 0;
    for (let q in answers) {
      let sel = document.querySelector(`input[name="${q}"]:checked`);
      if (sel && sel.value === answers[q]) score++;
    }
    document.getElementById('result').innerHTML = `🎉 Your Score: <b>${score} / 10</b>`;
  }
</script>
</body>
</html>
```

---

## Practical 23 – Student Marks Calculator (Grade + CSS Gradient)

```html
<!DOCTYPE html>
<html>
<head><title>Marks Calculator</title>
<style>
  body {
    font-family: Arial;
    background: linear-gradient(135deg, #667eea, #764ba2);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .container {
    background: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    width: 360px;
  }
  input { width: 100%; padding: 9px; margin: 6px 0 14px; box-sizing: border-box; border: 1px solid #ddd; border-radius: 5px; }
  button { background: #667eea; color: white; width: 100%; padding: 12px; border: none; border-radius: 8px; cursor: pointer; font-size: 16px; }
  button:hover { background: #764ba2; }
  #result { margin-top: 20px; padding: 15px; background: #f0f4ff; border-radius: 8px; text-align: center; display: none; }
</style>
</head>
<body>
<div class="container">
  <h2 style="text-align:center">Marks Calculator</h2>

  Name: <input type="text" id="sname" placeholder="Student name">
  Sub 1: <input type="number" id="s1" placeholder="Marks">
  Sub 2: <input type="number" id="s2" placeholder="Marks">
  Sub 3: <input type="number" id="s3" placeholder="Marks">
  Sub 4: <input type="number" id="s4" placeholder="Marks">
  Sub 5: <input type="number" id="s5" placeholder="Marks">

  <button onclick="calculate()">Calculate</button>

  <div id="result">
    <p id="rname"></p>
    <p id="rtotal"></p>
    <p id="rperc"></p>
    <p id="rgrade"></p>
  </div>
</div>

<script>
  function calculate() {
    let name = document.getElementById('sname').value;
    let marks = ['s1','s2','s3','s4','s5'].map(id => parseFloat(document.getElementById(id).value) || 0);
    let total = marks.reduce((a,b) => a+b, 0);
    let perc = (total / 500) * 100;
    let grade = perc >= 75 ? 'A' : perc >= 60 ? 'B' : perc >= 50 ? 'C' : 'F';

    document.getElementById('rname').innerHTML = '<b>Student:</b> ' + name;
    document.getElementById('rtotal').innerHTML = '<b>Total:</b> ' + total + ' / 500';
    document.getElementById('rperc').innerHTML = '<b>Percentage:</b> ' + perc.toFixed(2) + '%';
    document.getElementById('rgrade').innerHTML = '<b>Grade:</b> ' + grade;
    document.getElementById('result').style.display = 'block';
  }
</script>
</body>
</html>
```

---

## Practical 24 – PHP Feedback Form (with Date & Time)

**feedback.html**
```html
<!DOCTYPE html>
<html>
<head><title>Feedback Form</title>
<style>
  form { width: 380px; margin: 30px auto; font-family: Arial; background: white; padding: 25px; border-radius: 10px; box-shadow: 0 2px 10px #ccc; }
  input, textarea, select { width: 100%; padding: 8px; margin: 6px 0 14px; box-sizing: border-box; }
  button { background: #003080; color: white; padding: 10px; width: 100%; border: none; cursor: pointer; }
</style>
</head>
<body>
  <form action="feedback_process.php" method="POST">
    <h2>Feedback Form</h2>
    Name: <input type="text" name="name" required>
    Email: <input type="email" name="email" required>
    Rating:
    <select name="rating">
      <option>Excellent</option>
      <option>Good</option>
      <option>Average</option>
      <option>Poor</option>
    </select>
    Feedback: <textarea name="feedback" rows="4" required></textarea>
    <button type="submit">Submit Feedback</button>
  </form>
</body>
</html>
```

**feedback_process.php**
```php
<?php
  $name = $_POST['name'];
  $email = $_POST['email'];
  $rating = $_POST['rating'];
  $feedback = $_POST['feedback'];
  $datetime = date('l, d F Y – h:i:s A');
?>
<!DOCTYPE html>
<html>
<body style="font-family:Arial; padding:30px;">
  <h2>Thank You for Your Feedback!</h2>
  <p><b>Name:</b> <?= $name ?></p>
  <p><b>Email:</b> <?= $email ?></p>
  <p><b>Rating:</b> <?= $rating ?></p>
  <p><b>Feedback:</b> <?= $feedback ?></p>
  <hr>
  <p><b>Submitted on:</b> <?= $datetime ?></p>
  <a href="feedback.html">Submit Another</a>
</body>
</html>
```

---

*All codes are bare minimum and directly executable. HTML files open in browser. PHP files require XAMPP/localhost.*
