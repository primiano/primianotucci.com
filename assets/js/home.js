var wH = 0;
var bg = undefined;
var intro = undefined;

loadElements = function() {
  if (bg === undefined)
    bg = document.getElementById('bg');
  if (intro === undefined)
    intro = document.getElementById('intro');
}

fixViewportHeight = function() {
  loadElements();
  var newWH = window.innerHeight;
  if (Math.abs(newWH - wH) > 100) {
    var hStr = newWH + 'px';
    intro.style.height = hStr;
    bg.style.height = hStr;
  }
  wH = newWH;
}

// Terrible hack to workaround unstable viewport height on mobile browsers.
// See https://crbug.com/428132. It is a sad world.
if (window.innerWidth <= 640) {
  window.addEventListener('load', fixViewportHeight);
  window.addEventListener('resize', fixViewportHeight);
  fixViewportHeight();
}

// This would be a cool effect, but RAF is terribly inconsistent across browsers
// and the equivalent solution with CSS perspective creates all sort of jank
// and checkerboarding. It is a sad world (2).
// var bgY = 0;
// var rafCount = 0;
// updateBgParallax = function() {
//   loadElements();
//   var yScroll = window.scrollY
//   var yScroll = Math.max(yScroll, 0);
//   var newY = 250 * yScroll / (650 + yScroll);
//   if (newY == bgY)
//     return;
//   bgY = newY;
//   bg.style.transform  = 'translate3d(0px, -' + newY + 'px, 0px)';
// }
//
// animationFrameForBgParallax = function() {
//   if (rafCount-- <= 0)
//     return;
//   updateBgParallax();
//   window.requestAnimationFrame(animationFrameForBgParallax);
// }
//
// updateBgParallax();
// window.addEventListener('scroll',  function() {
//   rafCount = 3;
//   window.requestAnimationFrame(animationFrameForBgParallax);
// });
