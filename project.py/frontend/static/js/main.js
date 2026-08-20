/**
 * main.js — Student Performance Predictor
 * Handles: form UX, loading state, confidence bar animation
 */

document.addEventListener('DOMContentLoaded', function () {

    /* ── 1. Confidence Bar Animation (result page) ── */
    var bar = document.getElementById('confidenceBar');
    if (bar) {
        var targetWidth = bar.dataset.confidence || '0';
        setTimeout(function () {
            bar.style.width = targetWidth + '%';
        }, 300);
    }

    /* ── 2. Submit Button Loading State (index page) ── */
    var form = document.getElementById('predictForm');
    var btn  = document.getElementById('submitBtn');
    if (form && btn) {
        form.addEventListener('submit', function () {
            btn.disabled = true;
            btn.innerHTML =
                '<svg viewBox="0 0 24 24" class="spin" style="width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;">' +
                '<path d="M21 12a9 9 0 1 1-6.219-8.56"/></svg>' +
                ' Predicting...';
        });
    }

    /* ── 3. Input validation: highlight on invalid ── */
    var inputs = document.querySelectorAll('.form-control');
    inputs.forEach(function (input) {
        input.addEventListener('invalid', function () {
            input.style.borderColor = '#ef4444';
            input.style.boxShadow   = '0 0 0 3px rgba(239,68,68,0.15)';
        });
        input.addEventListener('input', function () {
            input.style.borderColor = '';
            input.style.boxShadow   = '';
        });
    });

});

/* ── Spinner CSS injected via JS to avoid extra <link> ── */
(function () {
    var style = document.createElement('style');
    style.textContent = '@keyframes spin { to { transform: rotate(360deg); } } .spin { animation: spin 0.8s linear infinite; }';
    document.head.appendChild(style);
})();
