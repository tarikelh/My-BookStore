import { Order_Product } from "./Order_Product";

export interface Order {
    id: number;
    order_date: string;
    state: string;
    total_order: number;
    user_id: number;
    products: Order_Product[]
}