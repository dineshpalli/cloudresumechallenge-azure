import { getVisitCount, updateCounter } from '../main';
import '@testing-library/jest-dom';

describe('Visitor Counter Functionality', () => {
  let fetchMock;
  let consoleSpy;

  beforeEach(() => {
    // Setup DOM
    document.body.innerHTML = `
      <div id="counter">Initial Count</div>
    `;

    // Mock fetch
    fetchMock = jest.fn();
    global.fetch = fetchMock;

    // Spy on console
    consoleSpy = jest.spyOn(console, 'error').mockImplementation(() => {});
  });

  afterEach(() => {
    jest.clearAllMocks();
    document.body.innerHTML = '';
  });

  test('getVisitCount successfully updates counter with API response', async () => {
    const mockResponse = { count: 100 };
    fetchMock.mockResolvedValueOnce({
      ok: true,
      json: () => Promise.resolve(mockResponse),
    });

    await getVisitCount('test-url');

    expect(document.getElementById('counter').textContent).toBe('100 Visit(s)');
    expect(fetchMock).toHaveBeenCalledWith('test-url');
  });

  test('getVisitCount handles network error', async () => {
    fetchMock.mockRejectedValueOnce(new Error('Network error'));

    await getVisitCount('test-url');

    expect(document.getElementById('counter').textContent).toBe('Unable to load visitor count.');
    expect(consoleSpy).toHaveBeenCalled();
  });

  test('updateCounter updates DOM element when it exists', () => {
    updateCounter('Test Message');
    expect(document.getElementById('counter').textContent).toBe('Test Message');
  });

  test('updateCounter handles missing DOM element', () => {
    document.body.innerHTML = ''; // Remove counter element
    const consoleSpyWarn = jest.spyOn(console, 'warn').mockImplementation(() => {});

    updateCounter('Test Message');

    expect(consoleSpyWarn).toHaveBeenCalledWith("No element with id 'counter' was found in the DOM.");
  });

  // NEW TEST: checks that the API response has a numeric "count" property
  // and the DOM displays it in "XXX Visit(s)" format.
  test('getVisitCount handles a numeric "count" property in API response', async () => {
    const mockResponse = { count: 210 };
    fetchMock.mockResolvedValueOnce({
      ok: true,
      json: () => Promise.resolve(mockResponse),
    });

    await getVisitCount('test-url');

    // Instead of checking exactly for "210 Visit(s)", verify the format
    expect(document.getElementById('counter').textContent).toMatch(/\d+\sVisit\(s\)/);
    expect(fetchMock).toHaveBeenCalledWith('test-url');
  });
});
