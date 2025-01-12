import '@testing-library/jest-dom';

describe('Theme Toggle Functionality', () => {
  beforeEach(() => {
    // Clear out the DOM
    document.body.innerHTML = '';

    // Set data-theme="dark" on the real <body>
    document.body.setAttribute('data-theme', 'dark');

    // Create and insert the toggle button + icon
    const button = document.createElement('button');
    button.className = 'theme-toggle';
    const icon = document.createElement('i');
    icon.className = 'fas fa-sun';
    button.appendChild(icon);
    document.body.appendChild(button);

    // Provide the toggleTheme function on window
    window.toggleTheme = function () {
      const body = document.body;
      const icon = document.querySelector('.theme-toggle i');

      if (body.getAttribute('data-theme') === 'dark') {
        body.removeAttribute('data-theme');
        icon.className = 'fas fa-moon';
      } else {
        body.setAttribute('data-theme', 'dark');
        icon.className = 'fas fa-sun';
      }
    };

    // Wire up the click event (this is crucial!)
    button.addEventListener('click', window.toggleTheme);
  });

  test('toggleTheme switches between light and dark themes', () => {
    const button = document.querySelector('.theme-toggle');
    const icon = document.querySelector('.theme-toggle i');

    // Initial state (dark theme)
    expect(document.body).toHaveAttribute('data-theme', 'dark');
    expect(icon).toHaveClass('fa-sun');

    // Toggle to light theme
    button.click();
    expect(document.body).not.toHaveAttribute('data-theme');
    expect(icon).toHaveClass('fa-moon');

    // Toggle back to dark theme
    button.click();
    expect(document.body).toHaveAttribute('data-theme', 'dark');
    expect(icon).toHaveClass('fa-sun');
  });
});
