<h2>1. robotalk.py</h2>

<strong>Description:</strong>  
<p>
  <code>robotalk.py</code> is a simple text-to-speech application that uses PowerShell commands to convert user input into speech. The user is prompted to enter text, and the script reads it aloud. The program terminates when specific keywords such as "quit", "shutup", "chup", or "shutdown" are entered, followed by a farewell message.
</p>

<strong>Key Features:</strong>
<ul>
  <li><strong>Text-to-Speech Conversion:</strong> Uses PowerShell's speech synthesis feature to convert text input into speech.</li>
  <li><strong>Graceful Exit:</strong> Recognizes specific commands ("quit", "shutup", "chup", "shutdown") to terminate the program with a closing message.</li>
</ul>

<strong>Usage:</strong>
<ol>
  <li>Run the script using Python:
    <pre><code>python robotalk.py</code></pre>
  </li>
  <li>Enter the text you want the script to speak.</li>
  <li>To exit the program, type any of the following commands: "quit", "shutup", "chup", or "shutdown".</li>
</ol>


<h2>2. youtubemanager.py</h2>

<strong>Description:</strong>  
<p>
  This script is a simple YouTube video manager that allows you to list, add, update, and delete video records stored in a JSON format (<code>youtube.txt</code> file).
</p>

<strong>Key Features:</strong>
<ul>
  <li>Load and save video data from/to a file.</li>
  <li>Add new videos with a name and duration.</li>
  <li>Update existing videos by index.</li>
  <li>Delete videos by index.</li>
  <li>User-friendly menu for interaction.</li>
</ul>

<strong>Usage:</strong>
<ol>
  <li>Run the script.</li>
  <li>Choose an option from the menu to manage the video records.</li>
</ol>

<h2>3. second_basic.py</h2>

<strong>Description:</strong>  
<p>
  This script includes various functionalities:
</p>
<ul>
  <li>A <code>car</code> class with static and instance methods.</li>
  <li>A <code>timer</code> decorator to measure the execution time of functions.</li>
  <li>Basic YouTube video management functions similar to <code>youtubemanager.py</code>.</li>
</ul>

<strong>Key Features:</strong>
<ul>
  <li><code>car</code> class with attributes and a method to display full details.</li>
  <li><code>timer</code> decorator to log the execution time of functions.</li>
  <li>Video management system with loading, adding, and listing videos.</li>
</ul>

<strong>Usage:</strong>
<ol>
  <li>Run the script.</li>
  <li>Use the <code>car</code> class or the YouTube manager as required by the code.</li>
</ol>

<h2>Requirements</h2>
<ul>
  <li>Python 3.x</li>
  <li>Keyboard library (for <code>robotalk.py</code>): Install using <code>pip install keyboard</code>.</li>
</ul>

<h2>How to Run</h2>
<ol>
  <li>Clone the repository or download the scripts.</li>
  <li>Make sure you have Python installed.</li>
  <li>Execute the desired script using the command:
    <pre><code>python &lt;script_name.py&gt;</code></pre>
  </li>
</ol>

<h2>License</h2>
<p>This project is licensed under the MIT License.</p>

