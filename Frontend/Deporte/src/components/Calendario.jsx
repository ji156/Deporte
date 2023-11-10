import { useEffect, useState } from "react";
import Navbar from "./Navbar";
import "../index.css";
import fondo from "../assets/img/campo.jpg";

function CalendarioLigaMasculina() {
  const [jornadas, setJornadas] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(
          "http://localhost:8000/calendario/api/calendario/laliga/"
        );
        const apiData = await response.json();

        const jornadasUnicas = Array.from(
          new Set(apiData.map((match) => match.jornada))
        );
        const jornadasOrdenadas = jornadasUnicas
          .map((jornada) => ({
            numero: jornada.replace("Jornada ", ""),
            partidos: apiData.filter((match) => match.jornada === jornada),
          }))
          .sort((a, b) => a.numero - b.numero);

        setJornadas(jornadasOrdenadas);
      } catch (error) {
        console.error("Error al obtener los datos de la API", error);
      }
    };

    fetchData();
  }, []);

  const formatTeamName = (str) => {
    if (!str) {
      return "";
    }
    return str
      .toLowerCase()
      .replace(/\s+/g, "")
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "");
  };

  return (
    <>
      <Navbar />
      <div
        className="calendario-container mt-5"
        style={{ backgroundImage: `url(${fondo})` }}
      >
        <div className="calendario-container mt-5">
          {jornadas.map((jornada) => (
            <div
              key={jornada.numero}
              className="jornada-container bg-gray-800 rounded-lg shadow-lg"
            >
              <h2 className="text-2xl font-bold pt-5">
                Jornada {jornada.numero}
              </h2>
              {/* Línea separadora */}
              <hr className="my-6 border-t border-gray-300 w-full z-10" />
              <ul className="partidos-list">
                {jornada.partidos.map((match) => (
                  <li key={match.id} className="partido-item">
                    <img
                      src={`http://localhost:8000/media/escudos/laliga/${formatTeamName(
                        match.local
                      )}.png`}
                      alt={`${match.local} logo`}
                      className="escudo-equipo"
                    />
                    <div className="local-team">{match.local}</div>
                    <div className="resultado">{match.resultado}</div>
                    <div className="visitante-team">{match.visitante}</div>
                    <img
                      src={`http://localhost:8000/media/escudos/laliga/${formatTeamName(
                        match.visitante
                      )}.png`}
                      alt={`${match.visitante} logo`}
                      className="escudo-equipo"
                    />
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </>
  );
}

export default CalendarioLigaMasculina;
