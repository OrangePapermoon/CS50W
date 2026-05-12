if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0);
}

function count() {
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector('h1').innerHTML = counter;
    localStorage.setItem('counter', counter);

}
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;
    // it's not count() because we're not calling the count function now
    // we're just setting the onclick property of the querySelector('button')
    // to count, which is just the name of the function
    // the count function is only called when the button is actually clicked
    // this is a paradigm of functional programming 

});