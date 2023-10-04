import React from 'react'
import logo from '../assets/images/logo.svg'
import main from '../assets/images/main.svg'

const Landing = () => {
  return (
    <main>
      <nav>
        <img src={logo} alt='jobify' className='logo'/>
      </nav>
      <div className='container page'>
        <div className='info'>
          <h1>
            Job <span>tracking</span> app
          </h1>
          <p>
          I'm baby authentic before they sold out cornhole blue bottle beard. Keffiyeh marxism blackbird 
          spyplane, vexillologist etsy art party same cold-pressed. Authentic skateboard organic cardigan
          vape neutra, yr banjo pour-over synth artisan lomo whatever hella pinterest. Austin marxism 
          flannel cardigan YOLO, irony everyday carry farm-to-table fit pinterest deep v neutra health goth.
          </p>
          <button className='btn btn-hero'>
            Login/Register
          </button>
        </div>
        <img src={main} alt='job hunter' className='img main-img'/>
      </div>
    </main>
  )
}

export default Landing