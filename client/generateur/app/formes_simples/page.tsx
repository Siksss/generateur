import { GenerateurFormesSimples } from "@/components/generateur_formes_simples"
import Navbar from "@/components/Navbar"

export default function About() {
  return (
  
        <main className="flex min-h-screen flex-col items-center pt-7 justify-between p-4 md:p-8">
          <header className="w-max max-w-5xl ">
            <Navbar />
          </header>
          <div className="w-full max-w-5xl">
            <GenerateurFormesSimples />
          </div>
        </main>
      )
}