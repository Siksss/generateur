"use client"

import { useRef, useState } from "react"
import { Card, CardContent } from "@/components/ui/card"
import { Slider } from "@/components/ui/slider"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"

export function GenerateurFormesSimples() {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const [sides, setSides] = useState(5)
  const [rotation, setRotation] = useState(0)
  const [size, setSize] = useState(100)
  const [color, setColor] = useState("#6366f1")
  const [imageURL, setImageURL] = useState<string | null>(null);
  // Fonction aleatoire
  const handleRandomize = () => {
    setSides(Math.floor(Math.random() * 10) + 3)
    setRotation(Math.floor(Math.random() * 360))
    setSize(Math.floor(Math.random() * 150) + 50)
    setColor(
      `#${Math.floor(Math.random() * 16777215)
        .toString(16)
        .padStart(6, "0")}`,
    )
  }
  // Envoie une requete POST à Flask pour generer le motif
  const handleFlaskGenerate = async () => {
    const response = await fetch("http://localhost:5000/generer_formes_simples", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        nbr_cote: sides,
        taille: size,
        angle: rotation,
        couleur: color,
      }),
    })
    // Si la requete est reussie, on recupere l'image et on l'affiche
    if (response.ok) {
      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      setImageURL(url);

    } else {
      console.error("Erreur lors de la génération du motif via Flask")
    }
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
      {/* Partie qui gere l'image */}
      <Card className="md:col-span-2">
        <CardContent className="p-6">
          <div className="flex justify-center items-center bg-gray-50 rounded-lg p-4">
            <div className="flex justify-center items-center bg-gray-50 rounded-lg p-4">
              {imageURL ? (
                <img src={imageURL} alt="Motif généré" className="border rounded shadow max-w-full" />
              ) : (
                <canvas ref={canvasRef} width={500} height={500} className="border border-gray-200 rounded-md shadow-sm" />
              )}
            </div>

          </div>
        </CardContent>
      </Card>
      {/* Partie qui gere les parametres */}
      <div className="space-y-6">
        <Tabs defaultValue="basic" className="w-full">
          <TabsList className="grid w-full grid-cols-2">
            <TabsTrigger value="basic">Paramètres</TabsTrigger>
            <TabsTrigger value="advanced">Avancé</TabsTrigger>
          </TabsList>
          <TabsContent value="basic" className="space-y-4 pt-4">
            <div className="space-y-2">
              <div className="flex justify-between">
                <Label htmlFor="sides">Nombre de côtés: {sides}</Label>
              </div>
              <Slider
                id="sides"
                min={3}
                max={20}
                step={1}
                value={[sides]}
                onValueChange={(value) => setSides(value[0])}
              />
            </div>

            <div className="space-y-2">
              <div className="flex justify-between">
                <Label htmlFor="rotation">Angle de rotation: {rotation}°</Label>
              </div>
              <Slider
                id="rotation"
                min={0}
                max={360}
                step={1}
                value={[rotation]}
                onValueChange={(value) => setRotation(value[0])}
              />
            </div>

            <div className="space-y-2">
              <div className="flex justify-between">
                <Label htmlFor="size">Taille: {size}px</Label>
              </div>
              <Slider
                id="size"
                min={10}
                max={250}
                step={1}
                value={[size]}
                onValueChange={(value) => setSize(value[0])}
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="color">Couleur</Label>
              <div className="flex gap-2">
                <div className="w-10 h-10 rounded-md border border-gray-200" style={{ backgroundColor: color }} />
                <Input
                  id="color"
                  type="color"
                  value={color}
                  onChange={(e) => setColor(e.target.value)}
                  className="w-full h-10"
                />
              </div>
            </div>
          </TabsContent>

          <TabsContent value="advanced" className="space-y-4 pt-4">           
            <div className="space-y-2">
              <Label htmlFor="sidesInput">Nombre de côtés (précis)</Label>
              <Input
                id="sidesInput"
                type="number"
                min={3}
                max={100}
                value={sides}
                onChange={(e) => setSides(Number.parseInt(e.target.value) || 3)}
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="rotationInput">Angle de rotation (précis)</Label>
              <Input
                id="rotationInput"
                type="number"
                min={0}
                max={360}
                value={rotation}
                onChange={(e) => setRotation(Number.parseInt(e.target.value) || 0)}
              />
            </div>
          </TabsContent>
        </Tabs>

        <div className="flex gap-2">
          <Button onClick={handleRandomize} className="flex-1">
            Aléatoire
          </Button>
          <Button onClick={handleFlaskGenerate} variant="secondary" className="flex-1">
            Générer via Flask
          </Button>
        </div>
      </div>
    </div>
  )
}