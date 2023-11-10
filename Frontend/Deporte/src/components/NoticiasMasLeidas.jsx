import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const NoticiasMasLeidas = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/noticias/api/noticias/")
      .then((response) => response.json())
      .then((apiData) => {
        // Ordenar por leidas en orden descendente
        const sortedData = apiData.sort((a, b) => b.leidas - a.leidas);
        // Tomar las primeras 5 noticias
        const top5 = sortedData.slice(0, 5);
        setData(top5);
      })
      .catch((error) => {
        console.error("Error al obtener los datos de la API", error);
      });
  }, []);

  return (
    <>
      <div className="relative min-h-screen">
        <h1 className="text-2xl underlin ml-3 pl-2 underline">
          Noticias más leídas
        </h1>
        <div className="noticias-container relative">
          {data.map((item) => (
            <Link
              to={`/noticias/${item.id}`}
              key={item.id}
              className="block mb-4"
            >
              <div
                className={`noticia rounded-lg shadow-lg border bg-custom-black p-4 font-bold w-80`}
              >
                <img
                  src={item.imagen}
                  alt="Imagen de la noticia"
                  className="mb-4 object-cover w-full h-48"
                />
                <h2 className="text-2xl font-semibold mb-2 text-white text-center">
                  {item.titulo}
                </h2>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </>
  );
};

export default NoticiasMasLeidas;
