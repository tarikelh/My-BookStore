import { Product } from './Product';

export interface Order_Product {
  order_id: number;
  product_id: number;
  quantity: number;
  product: Product;
}