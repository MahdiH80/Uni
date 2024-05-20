import React, { useEffect, useState } from "react";

export default function Tamrin_one() {
  const [data, setData] = useState([]);

  useEffect(() => {
    (async () => {
      try {
        const res = await fetch("https://fakestoreapi.com/products");
        const data = await res.json();
        setData(data);
      } catch (error) {
        console.error(error);
      }
    })();
  }, []);

  const items = data.map((e, index) => (
    <div key={index} className="card shadow" style={{ width: "18rem" }}>
      <img
        src={e.image}
        className="card-img-top"
        alt={e.title}
        style={{ width: "100$", height: "300px" }}
      />
      <div className="card-body">
        <h5 className="card-title">{e.title}</h5>
        <p className="card-text">
          {e.description.split(" ").slice(0, 5).join(" ")}
        </p>
      </div>
      <a href="#" className="btn btn-primary">
        Go somewhere
      </a>
    </div>
  ));

  return (
    <>
      <div className="d-flex justify-content-around flex-wrap shadow gap-3 container-fluid">
        {items}
      </div>
    </>
  );
}
