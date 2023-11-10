import { useEffect, useState } from "react";
import Navbar from "./Navbar";

function JornadaLigaMasculina() {
  const [data, setData] = useState([]);
  const [jornada, setJornada] = useState(1);

  useEffect(() => {
    fetch("http://localhost:8000/calendario/api/calendario/laliga/")
      .then((response) => response.json())
      .then((apiData) => {
        setData(apiData);
      })
      .catch((error) => {
        console.error("Error al obtener los datos de la API", error);
      });
  }, []);

  function formatTeamName(str) {
    if (!str) {
      return "";
    }
    return str
      .toLowerCase()
      .replace(/\s+/g, "")
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "");
  }

  useEffect(() => {
    if (data.length > 0 && data.length % 10 === 0) {
      setJornada((prevJornada) => prevJornada + 1);
    }
  }, [data]);

  const matchesByJornada = data.filter(
    (match) => match.jornada === `Jornada ${jornada}`
  );

  return (
    <>
      <Navbar />
      <div>
        <h2>Jornada {jornada}</h2>
        <ul>
          {matchesByJornada.map((match) => (
            <li key={match.id}>
              <p>
                {match.local} {match.resultado} {match.visitante}
              </p>
            </li>
          ))}
        </ul>
        <button onClick={() => setJornada((prevJornada) => prevJornada - 1)}>
          Jornada Anterior
        </button>
        <button onClick={() => setJornada((prevJornada) => prevJornada + 1)}>
          Siguiente Jornada
        </button>
      </div>
    </>
  );
}

export default JornadaLigaMasculina;
