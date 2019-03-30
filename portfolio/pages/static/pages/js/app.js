particlesJS('particles-js',
  {
    "particles": {
      "number": {
        "value": 55,
        "density": {
          "enable": true,
          "value_area": 700,
        }
      },
      "color": {
        "value": "#E8E8E8",
      },
      "shape": {
        "type": "circle",
        "stroke": {
          "width": 0.2,
          "color": "#181818",
        },
        "polygon": {
          "nb_sides": 5,
        },
      },
      "opacity": {
        "value": 0.6,
        "random": true,
        "anim": {
          "enable": true,
          "speed": 3,
          "opacity_min": 0.1,
          "sync": false
        }
      },
      "size": {
        "value": 6,
        "random": true,
        "anim": {
          "enable": false,
          "speed": 55,
          "size_min": 0.1,
          "sync": false
        }
      },
      "line_linked": {
        "enable": true,
        "distance": 140,
        "color": "#ffffff",
        "opacity": 0.42,
        "width": 0.8
      },
      "move": {
        "enable": true,
        "speed": 6,
        "direction": "none",
        "random": false,
        "straight": false,
        "out_mode": "out",
        "attract": {
          "enable": false,
          "rotateX": 600,
          "rotateY": 1200
        }
      }
    },
    "interactivity": {
      "detect_on": "canvas",
      "events": {
        "onhover": {
          "enable": true,
          "mode": "repulse"
        },
        "onclick": {
          "enable": true,
          "mode": "push"
        },
        "resize": true
      },
      "modes": {
        "grab": {
          "distance": 400,
          "line_linked": {
            "opacity": 1
          }
        },
        "bubble": {
          "distance": 200,
          "size": 5,
          "duration": 2,
          "opacity": 6,
          "speed": 2
        },
        "repulse": {
          "distance": 70
        },
        "push": {
          "particles_nb": 4
        },
        "remove": {
          "particles_nb": 2
        }
      }
    },
    "retina_detect": true,
  }

);
