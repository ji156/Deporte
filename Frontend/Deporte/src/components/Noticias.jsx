import Navbar from "./Navbar";
import { useEffect, useState } from "react";
import fondo from "../assets/img/campo.jpg";
import { Link } from "react-router-dom";

const Noticias = () => {
  const [data, setData] = useState([]);

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
  }, []);

  return (
    <>
      <Navbar className="fixed" />
      <div className="relative min-h-screen">
        <img
          src={fondo}
          alt="fondo"
          className="absolute inset-0 w-full h-full object-cover z-0"
        />
        <div className="noticias-container relative flex flex-wrap justify-center">
          {data.map((item) => (
            <Link to={`/noticias/${item.id}`} key={item.id}>
              <div className="noticia-container">
                <div
                  className={`noticia rounded-lg shadow-lg border bg-custom-black p-4 font-bold w-80 h-96 overflow-hidden mb-4`}
                >
                  <img
                    src={item.imagen}
                    alt="Imagen de la noticia"
                    className="mb-4 object-cover w-full h-48"
                  />
                  <h2 className="text-2xl font-semibold mb-2 text-white text-center overflow-hidden">
                    {item.titulo}
                  </h2>
                </div>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </>
  );
};

export default Noticias;
