import megusta from "../assets/img/me-gusta.png";
import nomegusta from "../assets/img/no-me-gusta.png";

const Comentarios = () => {
  return (
    <>
      <div className="flex flex-col items-center justify-center">
        {/* Comentarios */}
        <h1 className="text-2xl pl-3 p-2 w-2/4">2 Comentarios</h1>
        <div className="flex gap-16 mt-5">
          <h2>Todos</h2>
          <h2>Más valorados</h2>
          <h2>Menciones</h2>
        </div>
        {/* Línea separadora */}
        <hr className="my-6 border-t border-gray-300 w-full z-10" />
        <div>
          <div className="flex items-center justify-between mt-5 border-white p-4">
            <div className="flex items-center">
              <img
                src=""
                alt="img"
                className="rounded-full bg-white"
                style={{ width: "40px", height: "40px" }}
              />
              <div className="flex-col text-left ml-3">
                <p>Vikingo</p>
                <p>fecha</p>
              </div>
            </div>
            <p className="ml-auto">#1</p>
          </div>
          <p className="ml-16">Deja de llorar Shakiro</p>
          <div className="flex mt-5">
            <button className="mt-3 p-2 rounded-3xl ml-16 bg-slate-500">
              Responder
            </button>
            <button>
              <img
                src={megusta}
                alt="img"
                className="mt-3 p-2 rounded-3xl ml-16 bg-slate-500"
              />
            </button>
            <button>
              <img
                src={nomegusta}
                alt="img"
                className="mt-3 p-2 rounded-3xl ml-16 bg-slate-500"
              />
            </button>
          </div>
          {/* Línea separadora */}
          <hr className="my-6 border-t border-gray-300 w-full z-10" />
        </div>
        <div>
          <div className="flex items-center justify-between mt-5 border-white p-4">
            <div className="flex items-center">
              <img
                src=""
                alt="img"
                className="rounded-full bg-white"
                style={{ width: "40px", height: "40px" }}
              />
              <div className="flex-col text-left ml-3">
                <p>Imparcial</p>
                <p>fecha</p>
              </div>
            </div>
            <p className="ml-auto">#2</p>
          </div>
          <p className="ml-16">Tienes la 14 hasta la traquea payaso</p>
          <div className="flex mt-5">
            <button className="mt-3 p-2 rounded-3xl ml-16 bg-slate-500">
              Responder
            </button>
            <button>
              <img
                src={megusta}
                alt="img"
                className="mt-3 p-2 rounded-3xl ml-16 bg-slate-500"
              />
            </button>
            <button>
              <img
                src={nomegusta}
                alt="img"
                className="mt-3 p-2 rounded-3xl ml-16 bg-slate-500"
              />
            </button>
          </div>

          {/* Línea separadora */}
          <hr className="my-6 border-t border-gray-300 w-full z-10" />
        </div>
        <div className="flex">
          <div className="flex-grow p-5">
            <textarea
              placeholder="Escribe tu comentario"
              className="text-center resize-none w-full"
              style={{ overflow: "hidden", height: "1em" }}
              onInput={(e) => {
                e.target.style.height = "1em";
                e.target.style.height = `${e.target.scrollHeight}px`;
              }}
            ></textarea>
          </div>
          <button className="mt-3 p-2 rounded-3xl ml-2 bg-slate-500">
            Responder
          </button>
        </div>
      </div>
    </>
  );
};

export default Comentarios;
