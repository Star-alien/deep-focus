import React from 'react'
import Image from 'next/image'
import GoogleIcon from '../public/google_icon.png'

const GoogleSignIn = () => {
  return (
        <>
        <form action="" >
            <button 
            type='submit' 
            className='flex flex-row google-btn place-items-center text-[#051441] bg-white'>
            <Image src={GoogleIcon} width={30} className='mr-2 ml-32' alt='Google'/>
            Sign Up with Google
            </button>
        </form>
        
        </>
  )
}

export default GoogleSignIn
