import './App.css'
import {BrowserRouter, Route, Routes} from "react-router-dom";
import {Home} from "./pages/Home.tsx";
import {Detail} from "./pages/Detail.tsx";

function App() {

    return (
        <>
            <BrowserRouter>

                <Routes>
                    <Route path={"/"} Component={Home}/>
                    <Route path={"/works/:id"} Component={Detail}/>
                </Routes>
            </BrowserRouter>
        </>
    )
}

export default App
