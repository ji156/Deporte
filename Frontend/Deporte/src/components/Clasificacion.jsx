import { useEffect, useState } from "react";
import Navbar from "./Navbar";
import fondo from "../assets/img/campo.jpg";

function Clasificacion() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/clasificacion/api/clasificacion/")
      .then((response) => response.json())
      .then((apiData) => {
        const last20Results = apiData.slice(-20);
        setData(last20Results);
      })
      .catch((error) => {
        console.error("Error al obtener los datos de la API", error);
      });
  }, []);

  function formatTeamName(str) {
    return str
      .toLowerCase()
      .replace(/\s+/g, "")
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "");
  }

  return (
    <div
      className="min-h-screen bg-cover bg-center"
      style={{ backgroundImage: `url(${fondo})` }}
    >
      <Navbar />
      <div className="container mx-auto rounded-3xl bg-gray-800 shadow-lg mt-8 p-4">
        <h1 className="text-3xl font-semibold text-center text-white mb-4">
          Clasificación de la Liga
        </h1>
        <div className="overflow-x-auto">
          <table className="min-w-full bg-gray-800 rounded-lg shadow-lg text-white">
            <thead className="bg-indigo-700">
              <tr>
                <th className="p-2">Posición</th>
                <th className="p-2"></th>
                <th className="p-2 text-left">Equipo</th>
                <th className="p-2">Puntos</th>
                <th className="p-2">PJ</th>
                <th className="p-2">PG</th>
                <th className="p-2">PE</th>
                <th className="p-2">PP</th>
                <th className="p-2">GF</th>
                <th className="p-2">GC</th>
              </tr>
            </thead>
            <tbody className="text-center">
              {data.map((equipo) => {
                const formattedTeamName = formatTeamName(equipo.nombre_equipo);

                return (
                  <tr
                    key={equipo.id}
                    className="hover:bg-indigo-600 transition-all"
                  >
                    <td className="p-2">{equipo.posicion}</td>
                    <td className="p-2">
                      <img
                        src={`http://localhost:8000/media/escudos/laliga/${formattedTeamName}.png`}
                        alt={equipo.nombre_equipo}
                        className="w-8 h-8"
                        loading="lazy"
                      />
                    </td>
                    <td className="p-2 text-left">{equipo.nombre_equipo}</td>
                    <td className="p-2">{equipo.Puntos}</td>
                    <td className="p-2">{equipo.PJ}</td>
                    <td className="p-2">{equipo.PG}</td>
                    <td className="p-2">{equipo.PE}</td>
                    <td className="p-2">{equipo.PP}</td>
                    <td className="p-2">{equipo.GF}</td>
                    <td className="p-2">{equipo.GC}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Clasificacion;
