import {IndexIsLogin} from "../pages/IndexIsLogin.jsx";
import {IndexNotLogin} from "../pages/IndexNotLogin.jsx";
import {PrivateRoute} from "../components/PrivateRoute.jsx";

export function IndexLayout() {
    return (
        <PrivateRoute fallback={<IndexNotLogin />}>
          <IndexIsLogin />
        </PrivateRoute>
    );
}
