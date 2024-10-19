// Initialize CodeMirror with syntax highlighting and line numbers
var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
    lineNumbers: true,               // Enable line numbers
    mode: "javascript",              // Programming language (can change to others like 'python', 'htmlmixed')
    theme: "dracula",                // Optional: Apply the "dracula" theme (can change to other themes)
    tabSize: 2                       // Set the tab size for indentation
});

// Add event listener to the "Run Code" button
document.getElementById("run-btn").addEventListener("click", function() {
    const code = editor.getValue();   // Get the code from CodeMirror editor
    const resultFrame = document.getElementById("result");

    // Display the code output in the iframe
    resultFrame.srcdoc = code;
});

