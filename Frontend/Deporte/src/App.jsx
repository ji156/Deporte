import { BrowserRouter, Route, Routes } from "react-router-dom";
import Inicio from "./components/Inicio";
import Clasificacion from "./components/Clasificacion";
import CalendarioLigaMasculina from "./components/Calendario";
import Noticias from "./components/Noticias";
import Error404 from "./components/Error404";
import NoticiaDetalle from "./components/NoticiaDetalle";
import Registro from "./components/Registro";
import IniciarSesion from "./components/IniciarSesion";
import Terminos from "./components/Terminos";
import Hotjar from "@hotjar/browser";

const hotjarId = process.env.REACT_APP_HOTJAR_ID;
const hotjarScriptVersion = process.env.REACT_APP_HOTJAR_SCRIPT_VERSION;

if (hotjarId && hotjarScriptVersion) {
  Hotjar.initialize(hotjarId, hotjarScriptVersion);
}
const App = () => {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Inicio />} />
          <Route path="/inicio" element={<Inicio />} />
          <Route path="/clasificacion" element={<Clasificacion />} />
          <Route path="/calendario" element={<CalendarioLigaMasculina />} />
          <Route path="/noticias" element={<Noticias />} />
          <Route path="*" element={<Error404 />} />
          <Route path="/noticias/:id" element={<NoticiaDetalle />} />
          <Route path="/registro" element={<Registro />} />
          <Route path="/iniciar-sesion" element={<IniciarSesion />} />
          <Route path="/terminos-y-condiciones" element={<Terminos />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
};

export default App;
