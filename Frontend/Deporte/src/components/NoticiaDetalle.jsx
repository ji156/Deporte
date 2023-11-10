import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import Navbar from "./Navbar";
import NoticiasMasLeidas from "./NoticiasMasLeidas";
// import Comentarios from "./Comentarios";

const NoticiaDetalle = () => {
  const { id } = useParams();
  const [data, setData] = useState([]);
  const noticia = data.find((item) => item.id.toString() === id);

  useEffect(() => {
    // Realizar la solicitud a la API
    fetch("http://localhost:8000/noticias/api/noticias/")
      .then((response) => response.json())
      .then((apiData) => {
        setData(apiData);
      })
      .catch((error) => {
        console.error("Error al obtener los datos de la API", error);
      });
  }, [id]);

  if (!noticia) {
    return <div>Noticia no encontrada</div>;
  }

  return (
    <>
      <Navbar />
      <div className="container mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div className="p-8">
            <h2 className="text-5xl text-center font-bold mb-4">
              {noticia.titulo}
            </h2>
            <img
              className="mx-auto mb-8 rounded-lg"
              src={noticia.imagen}
              alt="Imagen de la noticia"
            />
            <p className="text-lg leading-7">
              {noticia.noticia.split("\n").map((paragraph, index) => (
                <p key={index} className="mb-4">
                  {paragraph}
                </p>
              ))}
            </p>
            {/* Línea separadora */}
            <hr className="my-6 border-t border-gray-300 w-full" />
            {/* Comentarios */}
            {/* <Comentarios /> */}
          </div>
          <div className="p-8">
            <NoticiasMasLeidas />
          </div>
        </div>
      </div>
    </>
  );
};

export default NoticiaDetalle;
