import { GenerateurFormesGeo } from "@/components/generateur_formes"

export default function Spirales() {
  return (
      <main className="flex min-h-screen flex-col items-center pt-7 justify-between p-4 md:p-8 mt-80">
        <div className="w-full max-w-5xl">
          <GenerateurFormesGeo />
        </div>
      </main>
    )
}