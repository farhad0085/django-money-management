import React from "react";
import TopNavigation from "../navigations/TopNavigation";


const LayoutContainer = ({ children }) => {
    return (
        <div>
            <TopNavigation />
            <div>
                {children}
            </div>
        </div>
    );
};

export default LayoutContainer;
