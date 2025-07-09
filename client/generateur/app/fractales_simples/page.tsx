import { GenerateurFractales } from "@/components/generateur_fractale"
import Navbar from "@/components/Navbar"

export default function Fractales() {
  return (
        <main className="flex min-h-screen flex-col items-center pt-7 justify-between p-4 md:p-8">
          <header className="w-max max-w-5xl ">
            <Navbar />
          </header>
          <div className="w-full max-w-5xl">
            <GenerateurFractales/>
          </div>
        </main>
      )
}