import { GenerateurFormesGeo } from "@/components/generateur_formes"
import Navbar from "@/components/Navbar"

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center pt-7 justify-between p-4 md:p-8">
      <div className="w-full max-w-5xl">
        <Navbar />
        <GenerateurFormesGeo />
      </div>
    </main>
  )
}

