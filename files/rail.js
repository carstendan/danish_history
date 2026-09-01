
(function(){
  var links = Array.prototype.slice.call(document.querySelectorAll('.rail a'));
  var map = {};
  links.forEach(function(a){ map[a.getAttribute('href').slice(1)] = a; });
  var targets = Object.keys(map).map(function(id){ return document.getElementById(id); })
                 .filter(Boolean);
  if(!('IntersectionObserver' in window) || !targets.length) return;
  var seen = {};
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){ seen[e.target.id] = e.isIntersecting ? e.boundingClientRect.top : null; });
    var best = null;
    targets.forEach(function(t){
      var r = t.getBoundingClientRect();
      if(r.top <= 140) best = t.id;
    });
    if(!best) best = targets[0].id;
    links.forEach(function(a){ a.classList.remove('active'); });
    if(map[best]) map[best].classList.add('active');
  }, {rootMargin:'-120px 0px -70% 0px', threshold:[0,1]});
  targets.forEach(function(t){ io.observe(t); });
  window.addEventListener('scroll', function(){
    var best = null;
    targets.forEach(function(t){ if(t.getBoundingClientRect().top <= 140) best = t.id; });
    if(!best) best = targets[0].id;
    links.forEach(function(a){ a.classList.remove('active'); });
    if(map[best]) map[best].classList.add('active');
  }, {passive:true});
})();
