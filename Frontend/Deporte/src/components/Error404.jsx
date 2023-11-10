import { Link } from "react-router-dom";

const Error404 = () => {
  return (
    <div className="h-screen flex flex-col justify-center items-center">
      <div className="ojos flex justify-center">
        <div className="eye pb-10">
          <div className="pupil"></div>
        </div>
        <div className="eye pb-10">
          <div className="pupil"></div>
        </div>
      </div>
      <div className="text-center p-10">
        <div className="text-white text-8xl">ERROR 404</div>
        <p className="text-white text-3xl pt-5 pb-5">Page not found</p>
        <button className="text-white font-bold py-2 px-4 rounded w-auto botonreturn">
          <Link to="/">
            <img src="#" alt="return" />
          </Link>
        </button>
      </div>
    </div>
  );
};

export default Error404;
