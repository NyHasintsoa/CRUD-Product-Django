/**
 * Back to top button
 */
let backtotop = select('.back-to-top')
if (backtotop) {
const toggleBacktotop = () => {
    if (window.scrollY > 100) {
        backtotop.classList.add('active')
    } else {
        backtotop.classList.remove('active')
    }
}
window.addEventListener('load', toggleBacktotop)
onscroll(document, toggleBacktotop)
}

/**
   * Initiate Bootstrap validation check
   */
var needsValidation = document.querySelectorAll('.needs-validation')

Array.prototype.slice.call(needsValidation)
    .forEach(function(form) {
        form.addEventListener('submit', function(event) {
        if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
        }

        form.classList.add('was-validated')
        }, false)
    })