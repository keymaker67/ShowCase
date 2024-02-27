import {Route, RedirectFunction} from "react-router-dom";

const PrivateRoute = ({children, ...rest}) => {
    console.log('private route works!')
    return(
        <Route {...rest}>{children}</Route>
    )
}

export default PrivateRoute