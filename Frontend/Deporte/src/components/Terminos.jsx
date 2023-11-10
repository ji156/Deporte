import { Link } from "react-router-dom";

const Terminos = () => {
  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="text-3xl mb-3 underline">
        <strong>Términos y Condiciones</strong>
      </h1>
      <p className="text-xl mb-7">
        <em>Fecha de última actualización: 09-11-2023</em>
      </p>
      <ol>
        <li>
          <strong>Aceptación de los Términos</strong>
          <p>
            Al acceder y utilizar este sitio web, usted acepta cumplir y estar
            sujeto a estos Términos y Condiciones. Si no está de acuerdo con
            alguno de estos términos, por favor, no utilice este sitio.
          </p>
        </li>
        <li>
          <strong>Uso del Sitio</strong>
          <p>
            Usted acepta utilizar este sitio únicamente para fines legales y de
            acuerdo con todos los reglamentos y leyes aplicables. Se prohíbe
            cualquier uso no autorizado o ilegal del sitio.
          </p>
        </li>
        <li>
          <strong>Propiedad Intelectual</strong>
          <p>
            Los contenidos, logotipos, gráficos y demás materiales en el sitio
            están protegidos por derechos de propiedad intelectual y no pueden
            ser utilizados sin el consentimiento previo y por escrito del
            propietario del sitio.
          </p>
        </li>
        <li>
          <strong>Privacidad</strong>
          <p>
            El uso de este sitio está sujeto a nuestra Política de Privacidad,
            que puede ser consultada <a href="#">aquí</a>.
          </p>
        </li>
        <li>
          <strong>Enlaces a Terceros</strong>
          <p>
            Este sitio puede contener enlaces a sitios web de terceros. No somos
            responsables de la precisión, contenido o políticas de privacidad de
            dichos sitios.
          </p>
        </li>
        <li>
          <strong>Limitación de Responsabilidad</strong>
          <p>
            No garantizamos la exactitud, integridad o actualidad de la
            información en este sitio. El uso de este sitio es bajo su propio
            riesgo.
          </p>
        </li>
        <li>
          <strong>Modificaciones</strong>
          <p>
            Nos reservamos el derecho de modificar estos Términos y Condiciones
            en cualquier momento. La fecha de la última actualización se
            indicará al principio de esta página.
          </p>
        </li>
        <li>
          <strong>Ley Aplicable</strong>
          <p>
            Estos Términos y Condiciones se rigen por las leyes de España y
            cualquier disputa estará sujeta a la jurisdicción de los tribunales
            de España.
          </p>
        </li>
      </ol>
      <Link to="/registro">
        <button className="mt-10 p-4 rounded-md bg-slate-700">Volver</button>
      </Link>
    </div>
  );
};

export default Terminos;
