const Footer = () => {
    const developer = "Elijah Abolaji"
    return (
        <div className="mt-8 text-center text-sm text-gray-500">
          <p>Supports MP4, AVI, MOV, MKV formats • Max file size: 100MB</p>
          <p className="mt-1">Your files are processed securely and deleted after conversion</p>
          <p className="mt-1"><strong>© {new Date().getFullYear()} | Developed By {developer}</strong></p>
        </div>
  )
}

export default Footer
