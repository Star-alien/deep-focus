'use client'


import React, { useState } from 'react'
import Image from 'next/image'
import logo from "@/public/deep-focus-logo.png"
import or from "@/public/or.png"
import GoogleSignIn from './GoogleSignIn'
import data from "../public/data"

const SignIn = () => {

  const [infos, setInfos] = useState(data)

  return (
    <>
    <div className='main'>
      <div className='login-section'>
        <Image 
        src={logo} 
        width={370} 
        height={40} 
        className='mx-20 my-10'
        alt='Deep Focus Logo'/>
        <div className='login-form grid mx-32'>
          <div className='my-5 p-3'>
            <h1 className='text-xl text-[#292C38] '><b>Welcome back to Deep Focus</b></h1>
            <p className='space-x-1 text-[#73778B]'>Sign In to continue...</p>
          </div>
          <GoogleSignIn />
          <Image src={or} width={500} height={21} className='mb-5' alt='or' />
          <form action="" >
            <input 
            type="text" 
            placeholder='Email' 
            className='login-input' 
            required/>

            <input 
            type="text" 
            placeholder='Password' 
            className='login-input' 
            required/>

            <button 
            type='submit' 
            className='sign-btn my-5'>
              Sign Up
            </button>
          </form>
          <div className='text-[#73778B] mt-3'>Don't have an account? <a className='text-[#3980ED] cursor-pointer'><b>Register</b></a></div>
        </div>
      </div>
      <div className='blue'>

      {infos.map((info) => {
        return(
          <div className='flex flex-row mb-6 ml-6' key={info.id} >
          <Image src={info.img} width={90} height={90} alt='Icon'/>
          <div className='ml-5'>
            <h1 className='text-lg'><b>{info.quality}</b></h1>
            <p>{info.paragraph}</p>
          </div>
        </div>
        )
      })}

      </div>
    </div>
    </>
  )
}

export default SignIn
