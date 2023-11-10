import { useEffect, useState } from "react";
import Navbar from "./Navbar";
import fondo from "../assets/img/campo.jpg";
import { Link } from "react-router-dom";

const API_URL = "http://localhost:8000/noticias/api/noticias/";

const Inicio = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Error de la API: ${response.status}`);
        }
        return response.json();
      })
      .then((apiData) => {
        setData(apiData);
      })
      .catch((error) => {
        console.error("Error al obtener los datos de la API", error);
        // Mostrar un mensaje de error al usuario si es necesario
      });
  }, []);

  const noticias = data.slice(0, 4);
  const noticias2 = data.slice(5, 9);

  return (
    <>
      <Navbar className="fixed" />
      <div
        className="bg-cover bg-center min-h-screen"
        style={{ backgroundImage: `url(${fondo})` }}
      >
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 p-4 mx-auto max-w-8xl">
          {noticias.length > 0 ? (
            <div className="lg:col-span-2 bg-white bg-opacity-80 rounded-lg shadow-md mx-auto w-full h-auto relative z-10 ">
              <div className="bg-opacity-50 w-full h-full rounded-lg p-3">
                <img
                  src={noticias[0].imagen}
                  alt="Imagen de la noticia principal"
                  className="w-full h-2/3 object-cover mb-4 rounded-lg"
                />
                <div className="h-1/3">
                  <p className="text-black text-2xl md:text-3xl lg:text-2xl text-left mb-1 ">
                    {noticias[0].tags}
                  </p>
                  <h2 className="text-3xl lg:text-3xl md:text-1xl font-bold mb-2 text-black text-left mt-5">
                    <Link to={`/noticias/${noticias[0].id}`}>
                      {noticias[0].titulo}
                    </Link>
                  </h2>
                </div>
              </div>
            </div>
          ) : (
            <p className="text-white">No hay noticias disponibles</p>
          )}

          <div className="lg:col-span-2">
            {noticias.slice(1).map((noticia) => (
              <div
                key={noticia.id}
                className="bg-white bg-opacity-80 p-2 rounded-lg shadow-md mb-2 flex flex-col md:flex-row"
              >
                <img
                  src={noticia.imagen}
                  alt="Imagen de la noticia"
                  className="w-full md:w-1/2 h-full object-cover rounded md:mr-4 mb-2 md:mb-0"
                />
                <div className="w-full md:w-1/2">
                  <p className="text-black md:text-lg lg:text-xl ">
                    {noticia.tags}
                  </p>
                  <h2 className="text-xl md:text-2xl lg:text-3xl font-bold mb-2 text-black ">
                    <Link to={`/noticias/${noticia.id}`}>{noticia.titulo}</Link>
                  </h2>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-2 lg:grid-cols-4 gap-4 p-4 mx-auto max-w-8xl">
          {noticias2.map((noticia) => (
            <div
              key={noticia.id}
              className="bg-white bg-opacity-80 p-2 rounded-lg shadow-md mb-2 flex flex-col md:flex-row"
            >
              <img
                src={noticia.imagen}
                alt="Imagen de la noticia"
                className="w-full md:w-1/2 h-full object-cover rounded md:mr-4 mb-2 md:mb-0"
              />
              <div className="w-full md:w-1/2">
                <p className="text-black md:text-lg lg:text-xl ">
                  {noticia.tags}
                </p>
                <h2 className="text-xl md:text-2xl lg:text-3xl font-bold mb-2 text-black ">
                  <Link to={`/noticias/${noticia.id}`}>{noticia.titulo}</Link>
                </h2>
              </div>
            </div>
          ))}
        </div>
      </div>
    </>
  );
};

export default Inicio;
