import { GenerateurFormesSimples } from "@/components/generateur_formes_simples"


export default function About() {
  return (
        <main className="flex min-h-screen flex-col items-center pt-7 justify-between p-4 md:p-8 mt-80">
          <div className="w-full max-w-5xl">
            <GenerateurFormesSimples />
          </div>
        </main>
      )
}